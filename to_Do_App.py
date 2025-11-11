import customtkinter as ctk

# === To Do App ===

root = ctk.CTk()
root.geometry("750x500")
root.title("Todo App")

def Add_To_do():
    to_do = entry.get()
    taskLabel = ctk.CTkLabel(scrolabalbeFrame, text=to_do, font=("Arial", 13))
    taskLabel.pack()
    entry.delete(0,ctk.END)


label = ctk.CTkLabel(root, text="Daily Routine task", font=("Helvetica Rounded", 20, 'bold'))
label.pack(pady=15)

scrolabalbeFrame = ctk.CTkScrollableFrame(root,width=600, height=300)
scrolabalbeFrame.pack()

entry = ctk.CTkEntry(scrolabalbeFrame,placeholder_text='Add your task', font=("Helvetica", 12))
entry.pack(fill='x', pady=5)


AddButton = ctk.CTkButton(root, text="Submit",width=600,height=30, font=("Helvetica", 14, 'bold'), command=Add_To_do)
AddButton.pack(pady= 15)

root.mainloop()