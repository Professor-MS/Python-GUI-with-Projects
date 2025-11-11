import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Pakistan Flag")


whiteSection = ttk.Label(root, text=" ", background="white")
whiteSection.pack(side='left', expand='True', fill='both')

GreenSec = ttk.Label(root, text=" ", background="green")
GreenSec.pack(side='left', expand='True', fill='both')
GreenSec2 = ttk.Label(root, text=" ", background="green")
GreenSec2.pack(side='left', expand='True', fill='both')



root.mainloop()