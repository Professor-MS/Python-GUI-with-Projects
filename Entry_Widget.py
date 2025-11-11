import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry('400x400')
root.title("Entry Widget Explanation")

icon = tk.PhotoImage(file="calculator.png")
root.iconphoto(True,icon)
# root.config(background="black")

# Entry Widget 
# entry_1 = ttk.Entry(root, width=40, show="*")
# entry_1 = ttk.Entry(root, width=40, state='readonly')

inputVar = tk.StringVar()
entry_1 = ttk.Entry(root, width=35, textvariable=inputVar, foreground="#00ff00", background='black')
bt_1 = ttk.Button(root, text='Click Now', padding=8, command= lambda: print(inputVar.get()))



entry_1.pack(pady=20)
bt_1.pack(pady=10)
root.mainloop()