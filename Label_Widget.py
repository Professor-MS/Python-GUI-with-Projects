import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('800x900')
root.title("Label")
root.config(background="#5cc3ff")

file_1 = tk.PhotoImage(file="deepseek.png")

# Label Widget

labelVariable = tk.StringVar(value="Subscribe Now")
label_1 = ttk.Label(root, 
                    text="Label widget", 
                    font=('Arial',28,"bold"),
                    background='black', 
                    foreground='#00ff00',
                    padding=(50,10),
                    # padding=20,
                    textvariable=labelVariable,
                    relief='sunken',
                    # relief='raised',
                    border=300,
                    image=file_1,
                    compound='bottom'
                    )

button_1 = ttk.Button(root, text='Subscribe', command= lambda: labelVariable.set('Subscribed'))

label_1.pack(pady=20)
button_1.pack()


root.mainloop()