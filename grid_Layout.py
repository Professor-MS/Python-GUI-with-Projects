import tkinter as tk
from tkinter import ttk
'''
Grid():
    -> grid() is something like table where we can arrange our widgets in row and colum.
    -> Options: rowspan and colspan.
    -> columnconfigure(1, weight=1)  rowconfigure(1, weight=1)
    -> grid(row=0, column= 0, sticky = "news") North, East, West, South
'''

root = tk.Tk()
root.geometry("300x300")
root.title("Grid Layout")

userNamLab = ttk.Label(root, text="Email: ",background='yellow')
userNamEntr = ttk.Entry(root)
PasswordLab = ttk.Label(root, text="Password: ", background='green')
PasswordEntr = ttk.Entry(root)
loginLabel = ttk.Button(root,text='Log In,')

# Creating Grid

# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=1)
root.columnconfigure((0,1),weight=1)
root.rowconfigure(0,weight=4)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

# Place widgets

userNamLab.grid(row=0,column=0, sticky='news')
userNamEntr.grid(row=0,column=1)
PasswordLab.grid(row=1,column=0,sticky='wens')
PasswordEntr.grid(row=1,column=1)
loginLabel.grid(row=2,column=0, sticky='nsew',columnspan=2)
root.mainloop()
