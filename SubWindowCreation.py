from tkinter import *

window =Tk()
window.title("New Window Creat")
window.geometry('200x200')
def CreateWindow():
    NewWindowTopLevel = Toplevel(background='red') #New window will be create on top of the other window, linked to the old window
    NewWindowTk = Tk() # New Independent window will be created, not linked to the old.
    # window.destroy()  # this will close the old window when new created through Tk()
Button(window, text="Create New Window", command=CreateWindow).pack(pady=25)

window.mainloop()