from tkinter import *
root = Tk()
root.geometry('700x700')

textArea = Text(root, width=60, height=20, font=("Ink Free", 14,'bold'),fg='red', bg='#aaddaa')
textArea.pack()

but = Button(root, text="Submit", font=("Ink Free", 14, 'bold'))
but.pack()

root.mainloop()
