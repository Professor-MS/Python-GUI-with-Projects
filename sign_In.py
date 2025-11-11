import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

MainWindow = ctk.CTk()
MainWindow.title("Sign in")
MainWindow.minsize(width=350,height=400)
MainWindow.maxsize(width=400,height=450)
# MainWindow.geometry("400x500")
'''
Sign In Label
email:
Password
Button Signing

'''
name = 'Salman'
passowrd = 123
def LogIn():
    email = emailEntry.get()
    passw = int(PassEntry.get())
    for widget in MainWindow.winfo_children():
        widget.destroy()
    if email==name and passw == passowrd:
        DoneLabel = ctk.CTkLabel(MainWindow,text="Log In Successful.")
        DoneLabel.pack()
    elif email!=name and passw == passowrd:
        DoneLabel = ctk.CTkLabel(MainWindow,text="Wrong Email.")
        DoneLabel.pack()
    elif email==name and passw != passowrd:
        DoneLabel = ctk.CTkLabel(MainWindow,text="Wrong Password.")
        DoneLabel.pack()
    else:
        NotDoneLabel = ctk.CTkLabel(MainWindow,text="Log In Faild.")
        NotDoneLabel.pack()
        goBack = ctk.CTkButton(MainWindow,text="Go Back")
        goBack.pack()

      
SignInLabel = ctk.CTkLabel(master=MainWindow, text="Sign In", font=("Helvetica", 24, "bold"))
SignInLabel.pack()
emailLabel = ctk.CTkLabel(master=MainWindow, text="Email", font=("Helvetica", 14, "bold"))
emailLabel.place(relx=0.1, rely=0.2)
emailEntry = ctk.CTkEntry(MainWindow,width=200)
emailEntry.place(relx=0.35, rely=0.2)


PassLabel = ctk.CTkLabel(master=MainWindow, text="Password", font=("Helvetica", 14, "bold"))
PassLabel.place(relx=0.1, rely=0.3)
PassEntry = ctk.CTkEntry(MainWindow,show="*", width=200)
PassEntry.place(relx=0.35, rely=0.3)


SignInButton = ctk.CTkButton(MainWindow, width=120,height=35, text="Sign In", command=LogIn)
SignInButton.place(relx=0.35, rely=0.5)


MainWindow.mainloop()
