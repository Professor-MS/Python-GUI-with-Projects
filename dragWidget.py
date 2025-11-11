from tkinter import *

window = Tk()
window.geometry('450x450')

def drag_Widget(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_Motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x #this function give us the top left X cordinates relative to the window
    y = widget.winfo_y() - widget.startY + event.y #this function give us the top left X cordinates relative to the window
    widget.place(x=x, y=y)


lab = Label(window, width=15, height=7,bg='red' )
lab.place(x=10, y=10)
lab1 = Label(window, width=15, height=7,bg='blue' )
lab1.place(x=150, y=150)


lab.bind("<Button-1>", drag_Widget)
lab.bind("<B1-Motion>", drag_Motion)
lab1.bind("<Button-1>", drag_Widget)
lab1.bind("<B1-Motion>", drag_Motion)


window.mainloop()