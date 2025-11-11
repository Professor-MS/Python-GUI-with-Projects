import customtkinter as ctk
from tkinter import filedialog, messagebox
import sqlite3
import threading
import csv
import os
from datetime import datetime, date, timedelta

# Optional notifications (safe fallback if missing)
try:
    from plyer import notification
except Exception:
    notification = None

# ---------------------- App Config ----------------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

DB_FILE = "tasks.db"

PRIORITIES = ["High", "Medium", "Low"]
RECURRENCE = ["None", "Daily", "Weekly", "Monthly"]

PRIORITY_COLOR = {"High": "#FF6B6B", "Medium": "#FFD166", "Low": "#06D6A0"}

# ---------------------- Data Layer ----------------------
class TaskDB:
    def __init__(self, path=DB_FILE):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            notes TEXT DEFAULT '',
            category TEXT DEFAULT 'General',
            priority TEXT DEFAULT 'Medium',
            due_date TEXT DEFAULT 'No Date',  -- YYYY-MM-DD or "No Date"
            completed INTEGER DEFAULT 0,
            recurrence TEXT DEFAULT 'None',    -- None/Daily/Weekly/Monthly
            remind_minutes_before INTEGER DEFAULT 0,
            sort_order INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS subtasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            sort_order INTEGER DEFAULT 0,
            FOREIGN KEY(task_id) REFERENCES tasks(id) ON DELETE CASCADE
        );
        """)
        # helpful indices
        cur.execute("CREATE INDEX IF NOT EXISTS idx_tasks_due ON tasks(due_date);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_tasks_completed ON tasks(completed);")
        self.conn.commit()

    # -------- Tasks CRUD --------
    def create_task(self, **t):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO tasks(title, notes, category, priority, due_date, completed,
                              recurrence, remind_minutes_before, sort_order)
            VALUES(?,?,?,?,?,?,?,?,?)
        """, (
            t.get("title","").strip(),
            t.get("notes","").strip(),
            t.get("category","General").strip(),
            t.get("priority","Medium"),
            t.get("due_date","No Date"),
            1 if t.get("completed", False) else 0,
            t.get("recurrence","None"),
            int(t.get("remind_minutes_before", 0) or 0),
            int(t.get("sort_order", 0)),
        ))
        self.conn.commit()
        return cur.lastrowid

    def update_task(self, task_id, **fields):
        if not fields: return
        cols = []
        vals = []
        for k,v in fields.items():
            cols.append(f"{k}=?")
            vals.append(v)
        cols.append("updated_at=CURRENT_TIMESTAMP")
        q = f"UPDATE tasks SET {', '.join(cols)} WHERE id=?"
        vals.append(task_id)
        self.conn.execute(q, tuple(vals))
        self.conn.commit()

    def delete_task(self, task_id):
        self.conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()

    def all_tasks(self):
        return self.conn.execute("SELECT * FROM tasks ORDER BY sort_order ASC, id ASC").fetchall()

    def get_task(self, task_id):
        return self.conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()

    # -------- Subtasks --------
    def add_subtask(self, task_id, title, sort_order=0):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO subtasks(task_id, title, sort_order) VALUES(?,?,?)",
                    (task_id, title.strip(), sort_order))
        self.conn.commit()
        return cur.lastrowid

    def list_subtasks(self, task_id):
        return self.conn.execute(
            "SELECT * FROM subtasks WHERE task_id=? ORDER BY sort_order ASC, id ASC", (task_id,)
        ).fetchall()

    def update_subtask(self, sub_id, **fields):
        if not fields: return
        cols, vals = [], []
        for k,v in fields.items():
            cols.append(f"{k}=?")
            vals.append(v)
        q = f"UPDATE subtasks SET {', '.join(cols)} WHERE id=?"
        vals.append(sub_id)
        self.conn.execute(q, tuple(vals))
        self.conn.commit()

    def delete_subtask(self, sub_id):
        self.conn.execute("DELETE FROM subtasks WHERE id=?", (sub_id,))
        self.conn.commit()

# ---------------------- UI ----------------------
class TodoApp:
    def __init__(self):
        self.db = TaskDB()
        self.root = ctk.CTk()
        self.root.title("🚀 Pro Task Manager")
        self.root.geometry("1100x720")
        self.root.minsize(900, 620)

        # Cache of task widgets: task_id -> dict(frame, checkbox, info_label, title_label)
        self.task_widgets = {}
        self.sort_mode = "Priority"  # or "Due", "A-Z"
        self.filter_priority = "All"
        self.filter_state = "All"     # All / Completed / Pending / Overdue
        self.search_query = ""

        self._build_ui()
        self._load_initial()
        self._schedule_reminders_thread()

    # ---------- Build UI ----------
    def _build_ui(self):
        top = ctk.CTkFrame(self.root)
        top.pack(fill="x", padx=10, pady=(10,6))

        self.title_lbl = ctk.CTkLabel(top, text="🚀 Pro Task Manager", font=("Helvetica Rounded", 24, "bold"))
        self.title_lbl.pack(side="left", padx=8)

        self.theme_btn = ctk.CTkButton(top, text="🌙", width=40, command=self.toggle_theme)
        self.theme_btn.pack(side="right", padx=4)

        self.help_btn = ctk.CTkButton(top, text="❓", width=40, command=self.show_help)
        self.help_btn.pack(side="right", padx=4)

        # Stats
        stats = ctk.CTkFrame(self.root)
        stats.pack(fill="x", padx=10, pady=(0,6))

        self.counter_label = ctk.CTkLabel(stats, text="Tasks: 0 Completed / 0 Pending", font=("Helvetica", 14))
        self.counter_label.pack(side="left", padx=8)

        self.progress = ctk.CTkProgressBar(stats, width=240)
        self.progress.set(0)
        self.progress.pack(side="right", padx=8)

        # Controls row
        controls = ctk.CTkFrame(self.root)
        controls.pack(fill="x", padx=10, pady=(0,8))

        self.search_entry = ctk.CTkEntry(controls, placeholder_text="🔍 Search title/notes/category...", width=360)
        self.search_entry.pack(side="left", padx=(6,6))
        self.search_entry.bind("<KeyRelease>", lambda e: self._set_search(self.search_entry.get()))

        self.state_filter = ctk.CTkOptionMenu(controls, values=["All","Pending","Completed","Overdue"],
                                              command=lambda _: self.refresh_list())
        self.state_filter.set("All")
        self.state_filter.pack(side="left", padx=6)

        self.pr_filter = ctk.CTkOptionMenu(controls, values=["All"]+PRIORITIES,
                                           command=lambda _: self.refresh_list())
        self.pr_filter.set("All")
        self.pr_filter.pack(side="left", padx=6)

        self.sort_menu = ctk.CTkOptionMenu(controls, values=["Priority","Due","A-Z"],
                                           command=self._set_sort)
        self.sort_menu.set("Priority")
        self.sort_menu.pack(side="left", padx=6)

        self.export_btn = ctk.CTkButton(controls, text="⬇ Export CSV", command=self.export_csv)
        self.export_btn.pack(side="right", padx=6)
        self.import_btn = ctk.CTkButton(controls, text="⬆ Import CSV", command=self.import_csv)
        self.import_btn.pack(side="right", padx=6)

        # Task list
        self.list_frame = ctk.CTkScrollableFrame(self.root, width=900, height=420)
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        # Add Task section
        add = ctk.CTkFrame(self.root)
        add.pack(fill="x", padx=10, pady=(0,10))

        self.title_entry = ctk.CTkEntry(add, placeholder_text="✍️ Task title", width=400)
        self.title_entry.pack(side="left", padx=(6,6))

        self.due_entry = ctk.CTkEntry(add, placeholder_text="📅 Due (YYYY-MM-DD)", width=170)
        self.due_entry.pack(side="left", padx=6)

        self.pr_option = ctk.CTkOptionMenu(add, values=PRIORITIES, width=120)
        self.pr_option.set("Medium")
        self.pr_option.pack(side="left", padx=6)

        self.cat_entry = ctk.CTkEntry(add, placeholder_text="🏷️ Category", width=140)
        self.cat_entry.pack(side="left", padx=6)

        self.rec_option = ctk.CTkOptionMenu(add, values=RECURRENCE, width=120)
        self.rec_option.set("None")
        self.rec_option.pack(side="left", padx=6)

        self.remind_entry = ctk.CTkEntry(add, placeholder_text="⏰ Remind min before (0)", width=170)
        self.remind_entry.pack(side="left", padx=6)

        self.add_btn = ctk.CTkButton(add, text="➕ Add Task", command=self.add_task)
        self.add_btn.pack(side="left", padx=6)

        # Clear All
        self.clear_btn = ctk.CTkButton(self.root, text="🧹 Clear All (Delete)", command=self.clear_all)
        self.clear_btn.pack(padx=10, pady=(0,8), anchor="w")

        # Enter to add
        self.root.bind("<Return>", lambda e: self.add_task())

    # ---------- Load / Refresh ----------
    def _load_initial(self):
        rows = self.db.all_tasks()
        for r in rows:
            self._add_task_widget(r)
        self._reorder_after_sort()
        self.update_stats()

    def _set_search(self, text):
        self.search_query = (text or "").strip().lower()
        self.refresh_list()

    def _set_sort(self, mode):
        self.sort_mode = mode
        self._reorder_after_sort()

    def refresh_list(self):
        # Show/hide frames based on search + filters
        self.filter_priority = self.pr_filter.get()
        self.filter_state = self.state_filter.get()
        for task_id, w in self.task_widgets.items():
            row = self.db.get_task(task_id)
            if not row: 
                continue
            visible = self._match_filters(row)
            if visible:
                w["frame"].pack(fill="x", padx=6, pady=4)
            else:
                w["frame"].pack_forget()
        self.update_stats()

    def _match_filters(self, row):
        # Search
        blob = " ".join([
            row["title"], row["notes"] or "", row["category"] or "", row["priority"] or "",
            row["due_date"] or ""
        ]).lower()
        if self.search_query and self.search_query not in blob:
            return False
        # Priority
        if self.filter_priority != "All" and row["priority"] != self.filter_priority:
            return False
        # State
        if self.filter_state != "All":
            if self.filter_state == "Completed" and row["completed"] != 1: return False
            if self.filter_state == "Pending" and row["completed"] == 1: return False
            if self.filter_state == "Overdue" and not self._is_overdue(row): return False
        return True

    # ---------- Create UI for a task ----------
    def _add_task_widget(self, row):
        task_id = row["id"]

        frame = ctk.CTkFrame(self.list_frame, corner_radius=12)
        frame.pack(fill="x", padx=6, pady=4)

        # Left: checkbox + title
        left = ctk.CTkFrame(frame)
        left.pack(side="left", fill="x", expand=True, padx=6, pady=6)

        chk = ctk.CTkCheckBox(left, text="", command=lambda tid=task_id: self.toggle_complete(tid))
        chk.pack(side="left", padx=(4,6))
        if row["completed"] == 1: chk.select()

        title_lbl = ctk.CTkLabel(left, text=row["title"], font=("Helvetica", 14))
        title_lbl.pack(side="left", padx=4)

        # Right: info + controls
        right = ctk.CTkFrame(frame)
        right.pack(side="right", padx=6, pady=6)

        info = ctk.CTkLabel(
            right,
            text=f"📅 {row['due_date']}  🏷️ {row['category']}  ⚠️ {row['priority']}  🔁 {row['recurrence']}",
            text_color=PRIORITY_COLOR.get(row["priority"], "white"),
            font=("Helvetica", 12)
        )
        info.pack(side="left", padx=6)

        # Reorder
        up_btn = ctk.CTkButton(right, text="⬆", width=30, command=lambda tid=task_id: self.bump_order(tid, -1))
        up_btn.pack(side="left", padx=2)
        down_btn = ctk.CTkButton(right, text="⬇", width=30, command=lambda tid=task_id: self.bump_order(tid, +1))
        down_btn.pack(side="left", padx=2)

        edit_btn = ctk.CTkButton(right, text="✏️", width=34, command=lambda tid=task_id: self.edit_task_dialog(tid))
        edit_btn.pack(side="left", padx=2)

        del_btn = ctk.CTkButton(right, text="🗑️", width=34, command=lambda tid=task_id: self.delete_task(tid))
        del_btn.pack(side="left", padx=2)

        # Subtasks toggle
        st_btn = ctk.CTkButton(right, text="📝 Subtasks", width=100, command=lambda tid=task_id: self.subtasks_dialog(tid))
        st_btn.pack(side="left", padx=6)

        self.task_widgets[task_id] = dict(frame=frame, checkbox=chk, info=info, title=title_lbl)

        # Style initial (overdue, completed)
        self._apply_style(task_id)

    # ---------- Styling ----------
    def _apply_style(self, task_id):
        row = self.db.get_task(task_id)
        if not row: return
        w = self.task_widgets[task_id]
        title = row["title"]
        if row["completed"] == 1:
            w["title"].configure(text=f"✔ {title}", text_color="gray")
        else:
            w["title"].configure(text=title, text_color="white")

        # Overdue highlight
        if self._is_overdue(row) and row["completed"] == 0:
            w["title"].configure(text_color="#FF4D4D")
        w["info"].configure(text_color=PRIORITY_COLOR.get(row["priority"], "white"),
                            text=f"📅 {row['due_date']}  🏷️ {row['category']}  ⚠️ {row['priority']}  🔁 {row['recurrence']}")

    def _is_overdue(self, row):
        d = self._parse_date(row["due_date"])
        return bool(d and date.today() > d)

    # ---------- Add / Edit / Delete ----------
    def add_task(self):
        title = (self.title_entry.get() or "").strip()
        if not title:
            messagebox.showwarning("Empty", "Task title is required.")
            return
        due = (self.due_entry.get() or "").strip() or "No Date"
        pr = self.pr_option.get()
        cat = (self.cat_entry.get() or "General").strip()
        rec = self.rec_option.get()
        try:
            remind = int((self.remind_entry.get() or "0").strip() or 0)
        except ValueError:
            remind = 0

        # sort_order -> max + 1
        rows = self.db.all_tasks()
        max_order = max([r["sort_order"] for r in rows], default=0) if rows else 0

        task_id = self.db.create_task(
            title=title, notes="", category=cat, priority=pr, due_date=due,
            completed=False, recurrence=rec, remind_minutes_before=remind,
            sort_order=max_order + 1
        )
        row = self.db.get_task(task_id)
        self._add_task_widget(row)
        self._reorder_after_sort()
        self._clear_add_inputs()
        self.update_stats()

    def _clear_add_inputs(self):
        self.title_entry.delete(0, ctk.END)
        self.due_entry.delete(0, ctk.END)
        self.cat_entry.delete(0, ctk.END)
        self.remind_entry.delete(0, ctk.END)
        self.pr_option.set("Medium")
        self.rec_option.set("None")

    def toggle_complete(self, task_id):
        row = self.db.get_task(task_id)
        if not row: return
        new_val = 0 if row["completed"] == 1 else 1
        self.db.update_task(task_id, completed=new_val)
        self._apply_style(task_id)
        self.update_stats()
        self.refresh_list()

        # If completing a recurring task, auto-generate next occurrence
        if new_val == 1 and row["recurrence"] != "None":
            self._spawn_next_recurrence(row)

    def edit_task_dialog(self, task_id):
        row = self.db.get_task(task_id)
        if not row: return
        dlg = ctk.CTkToplevel(self.root)
        dlg.title("Edit Task")
        dlg.geometry("460x480"); dlg.grab_set()

        # Inputs
        ctk.CTkLabel(dlg, text="Title").pack(pady=(12,0))
        e_title = ctk.CTkEntry(dlg); e_title.insert(0, row["title"]); e_title.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(dlg, text="Notes").pack()
        e_notes = ctk.CTkTextbox(dlg, height=90); e_notes.pack(fill="x", padx=12, pady=(0,8))
        e_notes.insert("1.0", row["notes"] or "")

        ctk.CTkLabel(dlg, text="Due (YYYY-MM-DD or blank)").pack()
        e_due = ctk.CTkEntry(dlg); e_due.insert(0, "" if row["due_date"]=="No Date" else row["due_date"]); e_due.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(dlg, text="Category").pack()
        e_cat = ctk.CTkEntry(dlg); e_cat.insert(0, row["category"] or "General"); e_cat.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(dlg, text="Priority").pack()
        e_pr = ctk.CTkOptionMenu(dlg, values=PRIORITIES); e_pr.set(row["priority"]); e_pr.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(dlg, text="Recurrence").pack()
        e_rec = ctk.CTkOptionMenu(dlg, values=RECURRENCE); e_rec.set(row["recurrence"]); e_rec.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(dlg, text="Remind minutes before (0=off)").pack()
        e_rem = ctk.CTkEntry(dlg); e_rem.insert(0, str(row["remind_minutes_before"] or 0)); e_rem.pack(fill="x", padx=12, pady=(0,8))

        def save():
            title = e_title.get().strip()
            if not title:
                messagebox.showwarning("Invalid", "Title cannot be empty.")
                return
            notes = e_notes.get("1.0", "end").strip()
            due = e_due.get().strip() or "No Date"
            cat = e_cat.get().strip() or "General"
            pr = e_pr.get()
            rec = e_rec.get()
            try:
                remind = int((e_rem.get() or "0").strip() or 0)
            except ValueError:
                remind = 0

            self.db.update_task(task_id,
                                title=title, notes=notes, due_date=due, category=cat,
                                priority=pr, recurrence=rec, remind_minutes_before=remind)
            self._apply_style(task_id)
            self.refresh_list()
            dlg.destroy()

        ctk.CTkButton(dlg, text="💾 Save", command=save).pack(pady=10)

    def delete_task(self, task_id):
        if not messagebox.askyesno("Confirm", "Delete this task?"): return
        self.db.delete_task(task_id)
        w = self.task_widgets.pop(task_id, None)
        if w: w["frame"].destroy()
        self.update_stats()

    def bump_order(self, task_id, delta):
        row = self.db.get_task(task_id)
        if not row: return
        new_order = max(0, row["sort_order"] + delta)
        self.db.update_task(task_id, sort_order=new_order)
        self._reorder_after_sort()

    # ---------- Subtasks ----------
    def subtasks_dialog(self, task_id):
        dlg = ctk.CTkToplevel(self.root)
        dlg.title("Subtasks")
        dlg.geometry("520x520"); dlg.grab_set()

        list_area = ctk.CTkScrollableFrame(dlg, height=360)
        list_area.pack(fill="both", expand=True, padx=8, pady=6)

        def refresh_list():
            for ch in list_area.winfo_children(): ch.destroy()
            subs = self.db.list_subtasks(task_id)
            for s in subs:
                rowf = ctk.CTkFrame(list_area); rowf.pack(fill="x", padx=4, pady=3)
                chk = ctk.CTkCheckBox(rowf, text=s["title"],
                                      command=lambda sid=s["id"]: self._toggle_subtask(sid))
                chk.pack(side="left", padx=6)
                if s["completed"] == 1: chk.select()
                ctk.CTkButton(rowf, text="✏️", width=34,
                              command=lambda sid=s["id"], ttl=s["title"]: self._edit_subtask(sid, ttl, refresh_list)).pack(side="right", padx=4)
                ctk.CTkButton(rowf, text="🗑️", width=34,
                              command=lambda sid=s["id"], rf=rowf: self._delete_subtask(sid, rf)).pack(side="right", padx=4)

        add_row = ctk.CTkFrame(dlg); add_row.pack(fill="x", padx=8, pady=6)
        e = ctk.CTkEntry(add_row, placeholder_text="Add subtask..."); e.pack(side="left", fill="x", expand=True, padx=4)
        ctk.CTkButton(add_row, text="➕ Add",
                      command=lambda: self._add_subtask(task_id, e, refresh_list)).pack(side="left", padx=4)

        refresh_list()

    def _add_subtask(self, task_id, entry_widget, refresh_cb):
        title = (entry_widget.get() or "").strip()
        if not title: return
        subs = self.db.list_subtasks(task_id)
        next_ord = max([s["sort_order"] for s in subs], default=0) + 1 if subs else 1
        self.db.add_subtask(task_id, title, next_ord)
        entry_widget.delete(0, ctk.END)
        refresh_cb()

    def _toggle_subtask(self, sub_id):
        sub = self._get_sub(sub_id)
        if not sub: return
        new_val = 0 if sub["completed"] == 1 else 1
        self.db.update_subtask(sub_id, completed=new_val)

    def _edit_subtask(self, sub_id, old_title, refresh_cb):
        dlg = ctk.CTkToplevel(self.root); dlg.title("Edit Subtask"); dlg.geometry("380x160"); dlg.grab_set()
        ctk.CTkLabel(dlg, text="Title").pack(pady=(12,0))
        e = ctk.CTkEntry(dlg); e.insert(0, old_title); e.pack(fill="x", padx=10, pady=(0,10))
        def save():
            t = e.get().strip()
            if t:
                self.db.update_subtask(sub_id, title=t)
                dlg.destroy(); refresh_cb()
        ctk.CTkButton(dlg, text="💾 Save", command=save).pack(pady=6)

    def _delete_subtask(self, sub_id, row_frame):
        if not messagebox.askyesno("Confirm", "Delete this subtask?"): return
        self.db.delete_subtask(sub_id)
        row_frame.destroy()

    def _get_sub(self, sub_id):
        return self.db.conn.execute("SELECT * FROM subtasks WHERE id=?", (sub_id,)).fetchone()

    # ---------- Sorting / Repack ----------
    def _reorder_after_sort(self):
        # Build list of widgets with sort keys
        items = []
        for tid, w in self.task_widgets.items():
            row = self.db.get_task(tid)
            if not row: continue
            items.append((tid, row))

        if self.sort_mode == "Priority":
            pr_rank = {"High": 0, "Medium": 1, "Low": 2}
            items.sort(key=lambda x: (pr_rank.get(x[1]["priority"], 3),
                                      self._date_key(x[1]["due_date"]),
                                      x[1]["completed"]))
        elif self.sort_mode == "Due":
            items.sort(key=lambda x: (self._date_key(x[1]["due_date"]),
                                      {"High":0,"Medium":1,"Low":2}.get(x[1]["priority"],2),
                                      x[1]["completed"]))
        else:  # A-Z
            items.sort(key=lambda x: (x[1]["title"].lower(), x[1]["completed"]))

        # Repack in new order; preserve visibility by filters
        for tid, _ in items:
            w = self.task_widgets[tid]
            w["frame"].pack_forget()
        for tid, row in items:
            w = self.task_widgets[tid]
            if self._match_filters(row):
                w["frame"].pack(fill="x", padx=6, pady=4)
        self.update_stats()

    def _date_key(self, s):
        d = self._parse_date(s)
        return d or date(9999,12,31)

    # ---------- Stats ----------
    def update_stats(self):
        total = len(self.task_widgets)
        completed = 0
        for tid in list(self.task_widgets.keys()):
            r = self.db.get_task(tid)
            if r and r["completed"] == 1: completed += 1
        pending = total - completed
        self.counter_label.configure(text=f"Tasks: {completed} Completed / {pending} Pending")
        self.progress.set(0 if total == 0 else completed/total)

    # ---------- Utils ----------
    def _parse_date(self, s):
        if not s or s == "No Date": return None
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            return None

    def toggle_theme(self):
        cur = ctk.get_appearance_mode()
        new_mode = "Dark" if cur == "Light" else "Light"
        ctk.set_appearance_mode(new_mode)
        self.theme_btn.configure(text="🌞" if new_mode == "Dark" else "🌙")

    def show_help(self):
        text = """📌 Pro Task Manager

• Add tasks with due date, category, priority, recurrence, and reminders
• Search + filter by state/priority; sort by Priority/Due/A-Z
• Subtasks + notes per task
• Reorder tasks with ⬆/⬇ (persists)
• Overdue tasks highlighted; recurring tasks auto-spawn next when completed
• Notifications require 'plyer' (optional)
• Export/Import CSV
• Auto-saves in SQLite (tasks.db)
"""
        messagebox.showinfo("Help", text)

    # ---------- CSV Export/Import ----------
    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if not path: return
        rows = self.db.all_tasks()
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id","title","notes","category","priority","due_date","completed","recurrence","remind_minutes_before","sort_order"])
            for r in rows:
                w.writerow([r["id"], r["title"], r["notes"], r["category"], r["priority"],
                            r["due_date"], r["completed"], r["recurrence"], r["remind_minutes_before"], r["sort_order"]])
        messagebox.showinfo("Export", "Exported successfully.")

    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV","*.csv")])
        if not path: return
        try:
            with open(path, "r", encoding="utf-8") as f:
                rd = csv.DictReader(f)
                for row in rd:
                    # Insert as new tasks ignoring incoming id
                    self.db.create_task(
                        title=row.get("title",""),
                        notes=row.get("notes",""),
                        category=row.get("category","General"),
                        priority=row.get("priority","Medium"),
                        due_date=row.get("due_date","No Date"),
                        completed=(row.get("completed","0") in ["1","True","true"]),
                        recurrence=row.get("recurrence","None"),
                        remind_minutes_before=int(row.get("remind_minutes_before","0") or 0),
                        sort_order=int(row.get("sort_order","0") or 0),
                    )
            # Rebuild UI
            for w in self.task_widgets.values(): w["frame"].destroy()
            self.task_widgets.clear()
            self._load_initial()
            messagebox.showinfo("Import", "Imported successfully.")
        except Exception as e:
            messagebox.showerror("Import Error", str(e))

    # ---------- Recurrence ----------
    def _spawn_next_recurrence(self, row):
        base = self._parse_date(row["due_date"]) or date.today()
        if row["recurrence"] == "Daily":
            nxt = base + timedelta(days=1)
        elif row["recurrence"] == "Weekly":
            nxt = base + timedelta(weeks=1)
        elif row["recurrence"] == "Monthly":
            # naive month add
            m = base.month + 1
            y = base.year + (m-1)//12
            m = (m-1)%12 + 1
            d = min(base.day, 28)  # keep safe
            nxt = date(y, m, d)
        else:
            return
        # create new pending task (same metadata)
        self.db.create_task(
            title=row["title"], notes=row["notes"], category=row["category"],
            priority=row["priority"], due_date=nxt.strftime("%Y-%m-%d"),
            completed=False, recurrence=row["recurrence"],
            remind_minutes_before=row["remind_minutes_before"],
            sort_order=(row["sort_order"] + 1)
        )
        # Quick refresh
        self._reload_list()

    def _reload_list(self):
        for w in self.task_widgets.values():
            w["frame"].destroy()
        self.task_widgets.clear()
        self._load_initial()
        self.refresh_list()

    # ---------- Reminders (Background) ----------
    def _schedule_reminders_thread(self):
        def worker():
            while True:
                try:
                    self._check_reminders()
                except Exception:
                    pass
                # sleep ~60s
                for _ in range(60):
                    # stop-friendly if window closed
                    if not self.root.winfo_exists(): return
                    self.root.after(1000, lambda: None)  # tick UI loop
                    self.root.update_idletasks()
        th = threading.Thread(target=worker, daemon=True)
        th.start()

    def _check_reminders(self):
        # notify when now >= (due - remind_minutes)
        now = datetime.now()
        rows = self.db.all_tasks()
        for r in rows:
            if r["completed"] == 1: continue
            if (r["remind_minutes_before"] or 0) <= 0: continue
            d = self._parse_date(r["due_date"])
            if not d: continue
            due_dt = datetime(d.year, d.month, d.day, 9, 0, 0)  # 9am default
            remind_dt = due_dt - timedelta(minutes=int(r["remind_minutes_before"]))
            if now >= remind_dt and now <= remind_dt + timedelta(minutes=1):
                self._notify(f"Task due soon: {r['title']}",
                             f"Category: {r['category']} • Priority: {r['priority']} • Due: {r['due_date']}")

    def _notify(self, title, message):
        if notification:
            try:
                notification.notify(title=title, message=message, timeout=5, app_name="Pro Task Manager")
            except Exception:
                print("[Notify]", title, "-", message)
        else:
            print("[Notify]", title, "-", message)

    # ---------- Helpers ----------
    def _parse_int(self, s, default=0):
        try: return int(s)
        except: return default

    # ---------- Clear All ----------
    def clear_all(self):
        if not messagebox.askyesno("Confirm", "Delete ALL tasks? This cannot be undone."):
            return
        self.db.conn.execute("DELETE FROM subtasks;")
        self.db.conn.execute("DELETE FROM tasks;")
        self.db.conn.commit()
        for w in self.task_widgets.values():
            w["frame"].destroy()
        self.task_widgets.clear()
        self.update_stats()

    # ---------- Window ----------
    def run(self):
        self.root.mainloop()

# ---------------------- Start ----------------------
if __name__ == "__main__":
    app = TodoApp()
    app.run()
