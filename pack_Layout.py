import tkinter as tk
from tkinter import ttk
"""
Layout:
    -> Laytout is responsible for the arrangment of widgets on the screen.
    -> There are three main layout managment:
            1. Pack()
            2. Grid()
            3. Place()
    Pack():
        -> This automatically arrange widgets in the container.
        -> Options such as (pady, padx, side, expand &  fill) can be used to control the packing behavior.
        -> It organize widgets in block format, automatically adjust size of widgets to fit the available space.
        -> Suitable for simple layout.
"""
root = tk.Tk()
root.geometry('500x500')
root.title("Pack function in GUI")

# Frames
frame1 =tk.Frame(root)
frame2 =tk.Frame(root)
frame21 =tk.Frame(frame2)
frame22 = tk.Frame(frame2)


label1 = ttk.Label(frame1, text='Label 1',background='red')
label2 = ttk.Label(frame1, text='Label 2',background='yellow')


label3 = ttk.Label(root, text='Label 3',background='green')

button1 = tk.Button(frame21, text="Button 1")
button2 = tk.Button(frame21, text="Button 2")
button3 = tk.Button(frame21, text="Button 3")

label4 = ttk.Label(frame22, text="Label 4",background='blue')

# Packing
label1.pack(expand='True',fill='both',side='left')
label2.pack(expand='True',fill='both',side='left')
frame1.pack(expand='True',fill='both')

label3.pack(expand='True', fill='both')

button1.pack(expand='True',fill='both')
button2.pack(expand='True',fill='both')
button3.pack(expand='True',fill='both')
frame21.pack(expand='True',fill='both',side='left')

label4.pack(expand='True', fill='both')
frame22.pack(expand='True', fill='both',side='left')
frame2.pack(expand='True',fill='both')

root.mainloop()