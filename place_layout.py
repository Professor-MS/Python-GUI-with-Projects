import tkinter as tk
from tkinter import ttk

'''
Place Layout:
    -> place() is related to the cordinate values (x-axis -> left side to right  , y-axis -> top to bottom).
    -> we have two option here:- absolute and relative

'''

rooot = tk.Tk()
rooot.geometry('500x400')
rooot.title("Place Layout in python gui")

label1 = ttk.Label(rooot, text='Label 1',background='yellow')
label3 = ttk.Label(rooot, text='Label 3',background='red')
label2 = ttk.Label(rooot, text='Label 2',background='green')


# label1.place(x=470, y=140,width=150, height=60) #Absolute position
# label3.place(x=470, y=140,width=100, height=40) #Absolute position
# label2.place(x=100, y=100,width=150, height=60,) #Absolute position
label1.place(relx=0.5, rely=0.3,relwidth=0.3, relheight=0.2) #Relative position
label3.place(relx=0.4, rely=0.2,relwidth=0.4, relheight=0.2) #Relative position
label2.place(relx=0.1, rely=0.4,relwidth=0.2, relheight=0.1) #Relative position




rooot.mainloop()