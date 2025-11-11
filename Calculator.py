import tkinter as tk
from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry('400x600')
window.title("Calculator")
# icon = tk.PhotoImage(file="Python.png")
# window.iconphoto(True,icon)
window.config(background="black")

# Button Click and Value should be displayed on the screen
def buttonClick(value):
    x = inputVar.get()
    inputVar.set(x+value)

def Calculate():
    try:
        Result = eval(inputVar.get())
        inputVar.set(Result)
    except Exception as e:
        inputVar.set(e)
def Backspace():
    inputVar.delete(len(inputVar.get())-1, END)
#  Calculator Display
inputVar = tk.StringVar()
display = ctk.CTkEntry(window,textvariable= inputVar, font=('Arial', 28), justify='right')
display.grid(row=0,column=0, columnspan=4,sticky='ewns',padx=15,pady=15)

# 7
SevenButton = ctk.CTkButton(window, text='7', command= lambda: buttonClick('7'))
SevenButton.grid(row=1,column=0,sticky='ewns',padx=5,pady=5)
# 8
EightButton = ctk.CTkButton(window, text='8', command= lambda: buttonClick('8'))
EightButton.grid(row=1,column=1,sticky='ewns',padx=5,pady=5)
# 9
NineButton = ctk.CTkButton(window, text='9', command= lambda: buttonClick('9'))
NineButton.grid(row=1,column=2,sticky='ewns',padx=5,pady=5)
# /
DividButton =ctk.CTkButton(window, text='/', command= lambda: buttonClick('/'))
DividButton.grid(row=1,column=3,sticky='ewns',padx=5,pady=5)

# 4
FourButton = ctk.CTkButton(window, text='4', command= lambda: buttonClick('4'))
FourButton.grid(row=2,column=0,sticky='ewns',padx=5,pady=5)
# 5
FiveButton = ctk.CTkButton(window, text='5', command= lambda: buttonClick('5'))
FiveButton.grid(row=2,column=1,sticky='ewns',padx=5,pady=5)
# 6
SixButton = ctk.CTkButton(window, text='6', command= lambda: buttonClick('6'))
SixButton.grid(row=2,column=2,sticky='ewns',padx=5,pady=5)
# /
MulButton = ctk.CTkButton(window, text='*', command= lambda: buttonClick('*'))
MulButton.grid(row=2,column=3,sticky='ewns',padx=5,pady=5)
# 1
OneButton = ctk.CTkButton(window, text='1', command= lambda: buttonClick('1'))
OneButton.grid(row=3,column=0,sticky='ewns',padx=5,pady=5)
# 2
TwoButton = ctk.CTkButton(window, text='2', command= lambda: buttonClick('2'))
TwoButton.grid(row=3,column=1,sticky='ewns',padx=5,pady=5)
# 3
ThreeButton = ctk.CTkButton(window, text='3', command= lambda: buttonClick('3'))
ThreeButton.grid(row=3,column=2,sticky='ewns',padx=5,pady=5)
# /
AddButton = ctk.CTkButton(window, text='+', command= lambda: buttonClick('+'))
AddButton.grid(row=3,column=3,sticky='ewns',padx=5,pady=5)
# 0
ZeroButton = ctk.CTkButton(window, text='0', command= lambda: buttonClick('0'))
ZeroButton.grid(row=4,column=0,sticky='ewns',padx=5,pady=5)
# .
DotButton = ctk.CTkButton(window, text='.', command= lambda: buttonClick('.'))
DotButton.grid(row=4,column=1,sticky='ewns',padx=5,pady=5)
# =
backspaceButton = ctk.CTkButton(window, text='Backspace', command= Backspace)
backspaceButton.grid(row=4,column=2,sticky='ewns',padx=5,pady=5)
# -
SubtractButton = ctk.CTkButton(window, text='-', command= lambda: buttonClick('-'))
SubtractButton.grid(row=4,column=3,sticky='ewns',padx=5,pady=5)
# Clear
ClearButton = ctk.CTkButton(window, text='C', command= lambda: inputVar.set(""))
ClearButton.grid(row=5,column=0,columnspan=2,sticky='ewns',padx=5,pady=5)
# Equal/ Answer
EqualButton = ctk.CTkButton(window, text='=', command= Calculate)
EqualButton.grid(row=5,column=2,sticky='ewns',columnspan=2,padx=5,pady=5)



# create 6 row
for i in range(6):
    window.rowconfigure(i, weight=1)

# creat 4 columns
for j in range(4):
    window.columnconfigure(j, weight=1)



window.mainloop()