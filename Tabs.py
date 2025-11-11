from tkinter import *
from tkinter import ttk


window =Tk()
window.title("Notebook")
window.geometry('500x500')

notebook = ttk.Notebook(window) #This manage a collection of windows/tabs/display 

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")

Label(tab1, text="Hello! This is Tab 1", font=("Ink Free", 35, 'bold')).pack()
Label(tab2, text="This is Tab 2 ", font=("Georgia", 35, 'bold')).pack()

notebook.pack(expand=True, fill='both')

window.mainloop()