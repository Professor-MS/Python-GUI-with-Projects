from tkinter import *

window = Tk()
window.geometry('450x200')

def doSomething(event):
    print("You click ",event)
    print("Mouse Coordinate: "+ str(event.x)+" , "+str(event.y))
window.bind("<Button-1>", doSomething) #left mouse click
# window.bind("<Button-2>", doSomething) #Scroll mouse wheel
# window.bind("<Button-3>", doSomething) #right mouse click
# window.bind("<ButtonRelease>", doSomething) #holding button release
# window.bind("<Enter>", doSomething) # enter to window
# window.bind("<Leave>", doSomething) # leave from window
# window.bind("<Motion>", doSomething) # Track mouse where it moved
window.mainloop()