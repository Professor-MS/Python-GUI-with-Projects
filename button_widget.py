import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('400x400')
root.title("Buttom Widget")

def clicked():
# def clicked(x):
    print("HELLO! YOU CLICKED THE BUTTON")
    print(buttonVariable.get())
    buttonVariable.set("Button Clicked")
    # print("Button clicked with arguments: ",x)

buttonVariable = tk.StringVar(value="Click This Button") #This is a special variable for updating current UI

# button1 = ttk.Button(root, text='This is Button',padding=10, command= lambda: print("Lambda Button is clicked"))   #Not Function Calling but print default line.
# button1 = ttk.Button(root, text='This is Button',padding=10, command=clicked)  #Simple Function Calling without parameter.
# button1 = ttk.Button(root, text='This is Button',padding=10, command=lambda: clicked(10))   #Function Calling with passing value. i.e x=10
button1 = ttk.Button(root, 
                     text = 'This is Button',
                     padding = 10,
                     command = clicked,
                     textvariable = buttonVariable)   #Function Calling with passing value. (i.e x=10) and Special Variable for Updating UI
button1.pack(pady = 20)

# -----------------------------

root.mainloop()
