import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("SpinBox ")


spinBox = ttk.Spinbox(window, width=30, from_=0, to=100, increment=1, command= lambda: print(spinBox.get()))
spinBox.pack()

window.mainloop()