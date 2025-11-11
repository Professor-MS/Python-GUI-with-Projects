from tkinter import *
from tkinter import filedialog
window = Tk()
window.geometry('650x300')
window.title("Menu")

def openFile():
    filePath = filedialog.askopenfilename()
    file = open(filePath,'r')
    print(file.read())
    file.close()
    
def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text file', '.txt'), ('HTML file', '.html'),('All file', '.*')])
    if file is None:
        return
    textInput = str(textArea.get('1.0', END))
    file.write(textInput)
    file.close()
    
def ExitFile():
    print("Exit Done")
    window.destroy()

def Copy():
    text = textArea.selection_get()
    print("Text Copied: ", text)

def Cut():
    print("Text Cut")


def Paste():
    print("Text Pasted")


menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile,font=("Impact", 14))
fileMenu.add_command(label="Save", command=saveFile,font=("MV Boli", 14))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=ExitFile, font=("Helvetica", 14))
# fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label="Copy", command=Copy,font=("Georgia", 14))
editMenu.add_command(label="Cut", command=Cut, font=("Arial", 14))
editMenu.add_separator()
editMenu.add_command(label="Paste", command=Paste, font=("Cascadia mono", 14))
editMenu.add_command(label="Adjust", command=Paste, font=("Lucida Handwriting", 14))
editMenu.add_command(label="Position", command=Paste, font=("Times New Roman", 14))
editMenu.add_command(label="Size", command=Paste, font=("Lucida Console", 14))


textArea = Text(window, )
textArea.pack()


window.mainloop()