from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
# # root.geometry('400x300')
# root.minsize(height=200, width=300)
# root.maxsize(height=400, width=400)
root.title("CheckBox and Radio Button")

# _______ Check Button ______
checkButtVar = tk.StringVar(value="Are you Agree?")
checkButton = ttk.Checkbutton(root, text='I agree', textvariable=checkButtVar)
checkButton.pack(pady=20)

# _______ Radio Button ______
# when we click on single option it select the all options, so the solution is to create a new variable and then bind the value of it with each and unique values.
optionVariable = tk.StringVar()
lab = Label(root, text="Select your Option?", font=('Helvetica', 16, 'bold'))
lab.pack()
radioButton1 = ttk.Radiobutton(root, text='Option 1', variable=optionVariable, value='option 1 selected', command= lambda: print(optionVariable.get()))
radioButton2 = ttk.Radiobutton(root, text='Option 2', variable=optionVariable, value='option 2 Selected', command= lambda: print(optionVariable.get()))
radioButton3 = ttk.Radiobutton(root, text='Option 3', variable=optionVariable, value='option 3 selected', command= lambda: print(optionVariable.get()))
radioButton4 = ttk.Radiobutton(root, text='Option 4', variable=optionVariable, value='option 4 selected', command= lambda: print(optionVariable.get()))
radioButton1.pack()
radioButton2.pack() 
radioButton3.pack()
radioButton4.pack()


# GenderVariable = tk.StringVar()
# MaleradioButton1 = ttk.Radiobutton(root, text='Male', variable=GenderVariable, value='M', command= lambda: print(GenderVariable.get()))
# FmaleradioButton2 = ttk.Radiobutton(root, text='Female', variable=GenderVariable, value='F', command= lambda: print(GenderVariable.get()))
# OtherradioButton3 = ttk.Radiobutton(root, text='Other', variable=GenderVariable, value='O', command= lambda: print(GenderVariable.get()))
# MaleradioButton1.pack()
# FmaleradioButton2.pack() 
# OtherradioButton3.pack()






root.mainloop()