import customtkinter as ctk
import os
from datetime import datetime
from tkinter import messagebox
import webbrowser

# === App Configuration ===
ctk.set_appearance_mode("System")  # Follows system theme
ctk.set_default_color_theme("blue")  # Modern blue theme

class TodoApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1000x700")
        self.root.title("Advanced Task Manager")
        self.root.minsize(800, 600)  # Minimum responsive size
        
        # File handling
        self.tasks_file = "tasks.txt"
        self.backup_dir = "task_backups"
        
        # Create backup directory if not exists
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        # Priority colors
        self.priority_colors = {
            "High": "#FF6B6B", 
            "Medium": "#FFD166", 
            "Low": "#06D6A0"
        }
        
        self.setup_ui()
        self.load_tasks()
        
        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)
    
    def setup_ui(self):
        """Initialize all UI components"""
        # Main container for responsive layout
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Header section
        self.header_frame = ctk.CTkFrame(self.main_frame)
        self.header_frame.pack(fill="x", pady=(0, 10))
        
        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="🚀 Advanced Task Manager", 
            font=("Helvetica Rounded", 24, 'bold')
        )
        self.title_label.pack(side="left", padx=10)
        
        # Theme switcher
        self.theme_btn = ctk.CTkButton(
            self.header_frame, 
            text="🌙", 
            width=40,
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="right", padx=5)
        
        # Help button
        self.help_btn = ctk.CTkButton(
            self.header_frame, 
            text="❓", 
            width=40,
            command=self.show_help
        )
        self.help_btn.pack(side="right", padx=5)
        
        # Stats frame
        self.stats_frame = ctk.CTkFrame(self.main_frame)
        self.stats_frame.pack(fill="x", pady=(0, 10))
        
        self.counter_label = ctk.CTkLabel(
            self.stats_frame, 
            text="Tasks: 0 Completed / 0 Pending", 
            font=("Helvetica", 14)
        )
        self.counter_label.pack(side="left", padx=10)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            self.stats_frame, 
            orientation="horizontal",
            width=200
        )
        self.progress_bar.pack(side="right", padx=10)
        self.progress_bar.set(0)
        
        # Search bar
        self.search_frame = ctk.CTkFrame(self.main_frame)
        self.search_frame.pack(fill="x", pady=(0, 10))
        
        self.search_entry = ctk.CTkEntry(
            self.search_frame, 
            placeholder_text='🔍 Search tasks...', 
            font=("Helvetica", 14), 
            width=400
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.search_entry.bind("<KeyRelease>", self.search_tasks)
        
        # Filter by priority
        self.filter_option = ctk.CTkOptionMenu(
            self.search_frame, 
            values=["All", "High", "Medium", "Low"],
            width=120,
            command=self.filter_by_priority
        )
        self.filter_option.set("All")
        self.filter_option.pack(side="right")
        
        # Tasks scrollable area
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame, 
            width=800,
            height=400
        )
        self.scrollable_frame.pack(fill="both", expand=True)
        
        # Input section
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill="x", pady=(10, 0))
        
        # Task entry
        self.entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text='✍️ Add your task...', 
            font=("Helvetica", 14)
        )
        self.entry.pack(fill="x", pady=5)
        
        # Due date and priority
        self.details_frame = ctk.CTkFrame(self.input_frame)
        self.details_frame.pack(fill="x")
        
        self.due_date_entry = ctk.CTkEntry(
            self.details_frame, 
            placeholder_text='📅 Due date (YYYY-MM-DD)', 
            font=("Helvetica", 12),
            width=200
        )
        self.due_date_entry.pack(side="left", padx=(0, 10))
        
        self.priority_option = ctk.CTkOptionMenu(
            self.details_frame, 
            values=["High", "Medium", "Low"],
            width=120
        )
        self.priority_option.set("Medium")
        self.priority_option.pack(side="left", padx=(0, 10))
        
        # Category
        self.category_entry = ctk.CTkEntry(
            self.details_frame, 
            placeholder_text='🏷️ Category', 
            font=("Helvetica", 12),
            width=150
        )
        self.category_entry.pack(side="left")
        
        # Add task button
        self.add_btn = ctk.CTkButton(
            self.input_frame, 
            text="➕ Add Task", 
            font=("Helvetica", 14, 'bold'), 
            command=self.add_task
        )
        self.add_btn.pack(fill="x", pady=5)
        
        # Bind Enter key to add task
        self.root.bind("<Return>", lambda event: self.add_task())
    
    # === Core Functionality ===
    def update_counter(self):
        """Update task statistics and progress bar"""
        total = 0
        completed = 0
        for frame in self.scrollable_frame.winfo_children():
            for widget in frame.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    total += 1
                    if widget.get() == 1:
                        completed += 1
        
        self.counter_label.configure(
            text=f"Tasks: {completed} Completed / {total - completed} Pending"
        )
        
        # Update progress bar
        if total > 0:
            progress = completed / total
            self.progress_bar.set(progress)
            
            # Change color based on completion
            if progress > 0.75:
                self.progress_bar.configure(progress_color="#06D6A0")  # Green
            elif progress > 0.5:
                self.progress_bar.configure(progress_color="#FFD166")  # Yellow
            else:
                self.progress_bar.configure(progress_color="#FF6B6B")  # Red
    
    def delete_task(self, frame):
        """Remove a task from the UI and save changes"""
        if messagebox.askyesno("Confirm", "Delete this task?"):
            frame.destroy()
            self.save_tasks()
            self.update_counter()
    
    def add_task(self):
        """Add a new task to the list"""
        task_text = self.entry.get().strip()
        due_date = self.due_date_entry.get().strip()
        priority = self.priority_option.get()
        category = self.category_entry.get().strip()
        
        if task_text:
            if not due_date:
                due_date = "No Date"
            if not category:
                category = "General"
            
            self.create_task(task_text, "0", priority, due_date, category)
            
            # Clear input fields
            self.entry.delete(0, ctk.END)
            self.due_date_entry.delete(0, ctk.END)
            self.category_entry.delete(0, ctk.END)
            
            self.save_tasks()
            self.update_counter()
    
    def create_task(self, task_text, status="0", priority="Medium", due_date="No Date", category="General"):
        """Create a new task widget"""
        frame = ctk.CTkFrame(self.scrollable_frame)
        frame.pack(fill="x", pady=2, padx=5)
        
        # Checkbox with task details
        task_details = f"{task_text}  📅 {due_date}  🏷️ {category}  ⚠️ {priority}"
        task = ctk.CTkCheckBox(
            frame, 
            text=task_details,
            command=self.update_counter,
            text_color=self.priority_colors.get(priority, "white"),
            font=("Helvetica", 12)
        )
        task.pack(side="left", padx=5, fill="x", expand=True)
        
        if status == "1":
            task.select()
        
        # Edit button
        edit_btn = ctk.CTkButton(
            frame, 
            text="✏️", 
            width=30,
            command=lambda f=frame: self.edit_task(f)
        )
        edit_btn.pack(side="right", padx=5)
        
        # Delete button
        delete_btn = ctk.CTkButton(
            frame, 
            text="❌", 
            width=30,
            command=lambda f=frame: self.delete_task(f)
        )
        delete_btn.pack(side="right", padx=5)
    
    def edit_task(self, frame):
        """Edit an existing task"""
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                current_text = widget.cget("text")
                parts = current_text.split("  ")
                
                # Extract components
                task_text = parts[0]
                due_date = parts[1].replace("📅 ", "")
                category = parts[2].replace("🏷️ ", "")
                priority = parts[3].replace("⚠️ ", "")
                
                # Create edit dialog
                edit_dialog = ctk.CTkToplevel(self.root)
                edit_dialog.title("Edit Task")
                edit_dialog.geometry("400x300")
                edit_dialog.grab_set()  # Make modal
                
                # Task entry
                ctk.CTkLabel(edit_dialog, text="Task:").pack(pady=(10, 0))
                task_entry = ctk.CTkEntry(edit_dialog, font=("Helvetica", 12))
                task_entry.insert(0, task_text)
                task_entry.pack(fill="x", padx=10, pady=(0, 10))
                
                # Due date
                ctk.CTkLabel(edit_dialog, text="Due Date:").pack()
                due_date_entry = ctk.CTkEntry(edit_dialog, font=("Helvetica", 12))
                due_date_entry.insert(0, due_date)
                due_date_entry.pack(fill="x", padx=10, pady=(0, 10))
                
                # Priority
                ctk.CTkLabel(edit_dialog, text="Priority:").pack()
                priority_option = ctk.CTkOptionMenu(
                    edit_dialog, 
                    values=["High", "Medium", "Low"],
                    font=("Helvetica", 12)
                )
                priority_option.set(priority)
                priority_option.pack(fill="x", padx=10, pady=(0, 10))
                
                # Category
                ctk.CTkLabel(edit_dialog, text="Category:").pack()
                category_entry = ctk.CTkEntry(edit_dialog, font=("Helvetica", 12))
                category_entry.insert(0, category)
                category_entry.pack(fill="x", padx=10, pady=(0, 10))
                
                # Save button
                def save_changes():
                    new_text = task_entry.get().strip()
                    new_due_date = due_date_entry.get().strip()
                    new_priority = priority_option.get()
                    new_category = category_entry.get().strip()
                    
                    if new_text:
                        widget.configure(
                            text=f"{new_text}  📅 {new_due_date}  🏷️ {new_category}  ⚠️ {new_priority}",
                            text_color=self.priority_colors.get(new_priority, "white")
                        )
                        self.save_tasks()
                        edit_dialog.destroy()
                
                save_btn = ctk.CTkButton(
                    edit_dialog, 
                    text="💾 Save Changes", 
                    command=save_changes
                )
                save_btn.pack(pady=10)
                
                break
    
    # === File Operations ===
    def save_tasks(self):
        """Save all tasks to file"""
        with open(self.tasks_file, "w") as file:
            for frame in self.scrollable_frame.winfo_children():
                for widget in frame.winfo_children():
                    if isinstance(widget, ctk.CTkCheckBox):
                        status = "1" if widget.get() == 1 else "0"
                        task_text = widget.cget("text")
                        
                        # Parse task details
                        parts = task_text.split("  ")
                        task_name = parts[0]
                        due_date = parts[1].replace("📅 ", "")
                        category = parts[2].replace("🏷️ ", "")
                        priority = parts[3].replace("⚠️ ", "")
                        
                        file.write(f"{task_name}|{status}|{priority}|{due_date}|{category}\n")
        
        # Create backup
        self.create_backup()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, "r") as file:
                    for line in file:
                        parts = line.strip().split("|")
                        if len(parts) == 5:
                            task_text, status, priority, due_date, category = parts
                            self.create_task(task_text, status, priority, due_date, category)
                        elif len(parts) >= 2:  # Backward compatibility
                            task_text, status = parts[0], parts[1]
                            priority = parts[2] if len(parts) > 2 else "Medium"
                            due_date = parts[3] if len(parts) > 3 else "No Date"
                            category = parts[4] if len(parts) > 4 else "General"
                            self.create_task(task_text, status, priority, due_date, category)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
        
        self.update_counter()
    
    def create_backup(self):
        """Create timestamped backup of tasks"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(self.backup_dir, f"tasks_{timestamp}.txt")
        
        try:
            with open(self.tasks_file, "r") as source, open(backup_file, "w") as target:
                target.write(source.read())
        except Exception as e:
            print(f"Backup failed: {str(e)}")
    
    # === Search and Filter ===
    def search_tasks(self, event=None):
        """Filter tasks based on search query"""
        query = self.search_entry.get().lower().strip()
        for frame in self.scrollable_frame.winfo_children():
            frame.pack_forget()  # Hide all first
            
        for frame in self.scrollable_frame.winfo_children():
            for widget in frame.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    task_text = widget.cget("text").lower()
                    if query in task_text:
                        frame.pack(fill="x", pady=2, padx=5)  # Show matching
    
    def filter_by_priority(self, priority):
        """Filter tasks by priority"""
        if priority == "All":
            for frame in self.scrollable_frame.winfo_children():
                frame.pack(fill="x", pady=2, padx=5)
        else:
            for frame in self.scrollable_frame.winfo_children():
                for widget in frame.winfo_children():
                    if isinstance(widget, ctk.CTkCheckBox):
                        task_text = widget.cget("text")
                        if f"⚠️ {priority}" in task_text:
                            frame.pack(fill="x", pady=2, padx=5)
                        else:
                            frame.pack_forget()
    
    # === UI Enhancements ===
    def toggle_theme(self):
        """Switch between light and dark mode"""
        current = ctk.get_appearance_mode()
        new_mode = "Dark" if current == "Light" else "Light"
        ctk.set_appearance_mode(new_mode)
        self.theme_btn.configure(text="🌞" if new_mode == "Dark" else "🌙")
    
    def show_help(self):
        """Display help information"""
        help_text = """📌 Advanced Task Manager Help:

• Add tasks with optional due dates and priorities
• Edit tasks by clicking the ✏️ button
• Search tasks using the search bar
• Filter by priority using the dropdown
• Tasks are automatically saved
• Dark/light mode toggle available

Keyboard Shortcuts:
Enter - Add new task
"""
        messagebox.showinfo("Help", help_text)
    
    def on_window_resize(self, event):
        """Handle window resize events"""
        # Adjust scrollable frame width
        new_width = self.main_frame.winfo_width() - 20
        if new_width > 100:
            self.scrollable_frame.configure(width=new_width)
        
        # Adjust search bar width
        search_width = self.search_frame.winfo_width() - 130
        if search_width > 100:
            self.search_entry.configure(width=search_width)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# === Run the Application ===
if __name__ == "__main__":
    app = TodoApp()
    app.run()