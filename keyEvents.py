from tkinter import *

window = Tk()
window.geometry('450x200')

def DisplayKey(event):
    labl.config(text=event.keysym)

# window.bind("<w>", DisplayKey)
# window.bind("<BackSpace>", DisplayKey)
window.bind("<Key>", DisplayKey)

labl = Label(window, font=("Impact", 60), pady=30)
labl.pack()
window.mainloop()