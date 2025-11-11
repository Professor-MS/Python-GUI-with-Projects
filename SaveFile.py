from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Save File")
root.geometry("400x300")
def Savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text file', '.txt'), ('HTML file', '.html'),('All file', '.*')])
    if file is None:
        return
    textInput = str(textArea.get('1.0', END))
    file.write(textInput)
    file.close()


SaveButton = Button(root, text="Save File", command=Savefile)
SaveButton.pack()
textArea = Text(root, background="#f2f3ae",padx=15, pady=5, foreground='red', font=('Ink Free', 25, 'bold'), width=50, height=10)
textArea.pack()

root.mainloop()