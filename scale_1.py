import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Scale ")

def DisplayValue(value):
    
    print("Hello",value)



scale1 = ttk.Scale(window, from_=0, to=300, length=300, orient='horizontal', command=DisplayValue)

scale1.pack() 


window.mainloop()