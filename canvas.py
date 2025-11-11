#canvas = it is a widget that is used to draw graphd, plots, images in a window
from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()


# canvas.create_line(0,0,250,250, width=5, fill='red')
# canvas.create_line(250,250,500,500, width=5, fill='blue')
# canvas.create_line(250,250,500,0, width=5, fill='yellow')
# canvas.create_line(0,500,250,250, width=5, fill='cyan')


# canvas.create_rectangle(200, 200, 400, 300, fill='purple')


# points = [250, 0, 500, 500,0,500]
# canvas.create_polygon(points,outline='yellow', width=5, fill='black')



# canvas.create_arc(0,0,500,500, fill='red', style = PIESLICE, start=0)
# canvas.create_arc(0,0,500,500, fill='green', style = PIESLICE, start=90)
# canvas.create_arc(0,0,500,500, fill='yellow', style = PIESLICE, start=180)
# canvas.create_arc(0,0,500,500, fill='blue', style = PIESLICE, start=270,
#                   # extent=180
#                   )



# canvas.create_arc(0,0,500,500, fill='red', extent=180, width=10)
# canvas.create_arc(0,0,500,500, fill='white', extent=180, start= 180, width=10)
# canvas.create_oval(190,190,310,310, fill='white', width=10)


root.mainloop()