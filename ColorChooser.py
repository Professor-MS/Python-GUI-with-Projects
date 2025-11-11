from tkinter import *
from tkinter import colorchooser

root = Tk()

root.title("Color Choser")
root.geometry("200x200")
def colorChoser():
    color= colorchooser.askcolor()
    # root.config(background=colorchooser.askcolor()[1])
    # root.config(background=color[1])
    hexColor = color[1]
    print(hexColor)
    root.config(background=hexColor)


colorButon = Button(root, text= "Choose Color", width=12, height=2, command=colorChoser)
colorButon.pack(pady=20)

root.mainloop()