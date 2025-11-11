from tkinter import *

root = Tk()
root.title("Frame")
root.geometry('400x400')
root.config(background="#AB0000")

frame = Frame(root, background='pink', bd=5, relief='raised')
frame.pack(side='bottom')
Button(frame, text="W", font=("Consolas", 24), width=3).pack(side="top")
Button(frame, text="A", font=("Consolas", 24), width=3).pack(side="left")
Button(frame, text="S", font=("Consolas", 24), width=3).pack(side='left')
Button(frame, text="D", font=("Consolas", 24), width=3).pack(side='left')


root.mainloop()