from tkinter import *


root = Tk()
root.geometry("500x500")
def movUp(event):
    canvas.move(img,0,-10)

def movDown(event):
    canvas.move(img,0,10)


def movLeft(event):
    canvas.move(img,-10,0)


def movRight(event):
    canvas.move(img,10,0)

root.bind("<Up>",movUp)
root.bind("<Down>",movDown)
root.bind("<Left>",movLeft)
root.bind("<Right>",movRight)
canvas = Canvas(root, width=500, height=500, background="#f3e77e") 
canvas.pack()

tractorImg = PhotoImage(file="tractor.png")
img = canvas.create_image(400,0,image=tractorImg, anchor=NW)



root.mainloop()