from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open File")
root.geometry("200x200")

def openFile():
    filePath = filedialog.askopenfilename(initialdir="C:\\Users\\Professor\\Desktop", filetypes=(("Text files", "*.txt"), ("All Files", "*.*"))) #this will open file in desktop and first looking txt file and then you can set to all file.
    fileText = open(filePath, 'r')
    print(fileText.read())
    fileText.close()


openButton = Button(root, command=openFile, text="Open file")
openButton.pack()
root.mainloop()