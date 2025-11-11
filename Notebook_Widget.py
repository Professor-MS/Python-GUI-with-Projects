# Notebook widget is something like there is a window having different tab and there should be different fram for each tab.
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("600x500")
root.title("Notebook Widget")


Notebook = ttk.Notebook(root)

frame_1 = ttk.Frame(Notebook)
frame_2 = ttk.Frame(Notebook)
frame_3 = ttk.Frame(Notebook)

Notebook.add(frame_1, text="Personal Info")
Notebook.add(frame_2, text="Education")
Notebook.add(frame_3, text="Address")

Label1 = ttk.Label(frame_1, text="Personal Info")
Label2 = ttk.Label(frame_2, text="Education")
Label3 = ttk.Label(frame_3, text="Address")
Label1.pack()
Label2.pack()
Label3.pack()

Notebook.pack(expand='True', fill='both')

 
root.mainloop()