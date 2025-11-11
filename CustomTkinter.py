import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("System")   #Dark  Light  System
ctk.set_default_color_theme("dark-blue")   # blue  green

root = ctk.CTk()
root.geometry("400x300")
root.title("Log In")


def LogIn():
    user = UserNameEntry.get()
    pwd = UserPasswordEntry.get()
    print(f"Username: {user}, Password: {pwd}")

userName = ctk.CTkLabel(root, text='Username: ')
userName.pack(pady=10)

UserNameEntry = ctk.CTkEntry(root)
UserNameEntry.pack()

userPass = ctk.CTkLabel(root, text='Password')
userPass.pack(pady=10)
UserPasswordEntry = ctk.CTkEntry(root, show='*')
UserPasswordEntry.pack()

LoginButton = ctk.CTkButton(root, text="Log In", command= LogIn)
LoginButton.pack(pady=20)


root.mainloop()