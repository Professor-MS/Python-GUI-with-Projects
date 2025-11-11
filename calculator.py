import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.title("Calculator")

# Functions
def add():
    a =int(num1.get())
    b = int(num2.get())
    sum = a+b
    print('Sum: ',sum)


def sub():
    a =int(num1.get())
    b = int(num2.get())
    subt = a-b
    print('Subtraction: ',subt)


def div():
    a =int(num1.get())
    b = int(num2.get())
    divid = a/b
    print('Division: ',divid)


def mul():
    a =int(num1.get())
    b = int(num2.get())
    mult = a*b
    print('Multiplication: ',mult)



# Frames
frameButtons = ttk.Frame(root)


# widgets
num1Label = ttk.Label(root, text="Enter first Number: ")
num1 = ttk.Entry(root,width=40)
num2Label = ttk.Label(root, text="Enter second Number: ")
num2 = ttk.Entry(root,width=40)
bt1 = ttk.Button(frameButtons, text='+',command=add)
bt2 = ttk.Button(frameButtons, text='-',command=sub)
bt3 = ttk.Button(frameButtons, text='/',command=div)
bt4 = ttk.Button(frameButtons, text='x',command=mul)



# Packing
num1Label.pack(pady=10)
num1.pack(pady=10)
num2Label.pack(pady=10)
num2.pack(pady=10)

bt1.pack(side='left',expand='True',fill='x')
bt2.pack(side='left',expand='True',fill='x')
bt3.pack(side='left',expand='True',fill='x')
bt4.pack(side='left',expand='True',fill='x')
frameButtons.pack(pady=15, expand="True", fill="both")
root.mainloop()