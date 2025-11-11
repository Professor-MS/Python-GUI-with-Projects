from tkinter import *
import time
root = Tk()

#Constant
WIDTH = 500
HEIGHT = 500

xVilocity = 3
yVilocity = 2
 
root.geometry("550x550")

canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="#6ed1ff")
canvas.pack()

earth = PhotoImage(file="earth.png")

EarthImg = canvas.create_image(0,0, image=earth, anchor=NW)
airplane = PhotoImage(file="airplane.png")
img = canvas.create_image(0,0, image=airplane, anchor=NW)

imageWidth = airplane.width()
imageHeight = airplane.height()
# print(imageWidth, imageHeight)

while True:
    cordinates = canvas.coords(img)
    print(cordinates)
    # canvas.move(img, xVilocity, 0)
    # canvas.move(img, 0, yVilocity)
    if(cordinates[0]>= (WIDTH-imageWidth) or cordinates[0]<0):
        xVilocity = -xVilocity
    if(cordinates[1]>= (HEIGHT-imageHeight) or cordinates[1]<0):
        yVilocity = -yVilocity
    canvas.move(img, xVilocity, yVilocity)
    root.update()
    time.sleep(0.01)


root.mainloop()