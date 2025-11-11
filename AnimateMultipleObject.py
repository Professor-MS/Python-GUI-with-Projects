from tkinter import * 
from ball import *
import time

WIDTH = 500
HEIGHT = 500
root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

volleyBall = Ball(canvas, 0,0,100,1,1,'white')
tenisBall = Ball(canvas, 0,0,50,4,3,'red')
basketBall = Ball(canvas, 0,0,125,8,7,'orange')

while True:
    volleyBall.move()
    tenisBall.move()
    basketBall.move() 
    root.update()
    time.sleep(0.01)


root.mainloop()