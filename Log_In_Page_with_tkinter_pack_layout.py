import tkinter as tk
from tkinter import ttk
# ctk.set_appearance_mode("System")   #Dark  Light  System
# ctk.set_default_color_theme("dark-blue")   # blue  green

root = tk.Tk()
root.geometry("400x300")
root.title("Log In")


def LogIn():
    user = UserNameEntry.get()
    pwd = UserPasswordEntry.get()
    print(f"Username: {user}, Password: {pwd}")

userName = ttk.Label(root, text='Username: ')
userName.pack(pady=10)

UserNameEntry = ttk.Entry(root)
UserNameEntry.pack()

userPass = ttk.Label(root, text='Password')
userPass.pack(pady=10)
UserPasswordEntry = ttk.Entry(root, show='*')
UserPasswordEntry.pack()

LoginButton = ttk.Button(root, text="Log In", command= LogIn)
LoginButton.pack(pady=20)


root.mainloop()