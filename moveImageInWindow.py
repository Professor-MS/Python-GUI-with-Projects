from tkinter import *

root = Tk()
root.geometry("500x500")

def movUp(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def movDown(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def movLeft(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def movRight(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


root.bind("<Up>",movUp)
root.bind("<Down>",movDown)
root.bind("<Left>",movLeft)
root.bind("<Right>",movRight)


tractorImg = PhotoImage(file="tractor.png")
label = Label(root, image=tractorImg)
label.place(x=400,y=10)


root.mainloop()