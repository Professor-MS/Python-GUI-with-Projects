from tkinter import *

window = Tk()
window.geometry('300x200')
stringV=StringVar()

label = Label(window, text='label', textvariable=stringV,font=("Ink Free", 18, 'bold'))
label.pack()

Entry(window, textvariable=stringV).pack()

window.mainloop()

