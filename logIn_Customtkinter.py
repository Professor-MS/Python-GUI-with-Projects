import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")



root = ctk.CTk()
root.geometry("300x400")
root.title("Log In")

def dashboard():
    neWin = ctk.CTk()
    neWin.geometry("300x400")
    neWin.title("Successfull Log In")

    UserName = ctk.CTkLabel(neWin,text="Name: Muhammad Salman")
    Department = ctk.CTkLabel(neWin,text="Department: Computer Science")
    UserName.pack()
    Department.pack(pady=10)
    neWin.mainloop()

def signIn():
    email = emailEntry.get()
    pasword = passEntry.get()
    print(f"\n\nYour Email is: {email}, \nYour Password is: {pasword}\n\n")
    dashboard()

emailLabel = ctk.CTkLabel(root,text='Email: ')
emailLabel.pack(pady=20)
emailEntry = ctk.CTkEntry(root, width=200, height=35)
emailEntry.pack()
passLabel = ctk.CTkLabel(root,text='Password: ')
passEntry = ctk.CTkEntry(root, show="*",width=200, height=35)
passLabel.pack()
passEntry.pack()

signInbt = ctk.CTkButton(root, text="Sign In", width=200, height=35, command=signIn)
signInbt.pack(pady=20)
root.mainloop()