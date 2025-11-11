# text: function like a text area, you can enter multiple lines of text
from tkinter import *
root = Tk()
root.title("Text Widget")
# root.geometry("400x400")

def display():
    textInput = textArea.get('1.0', END)
    print(textInput)
textArea = Text(root, background="#f2f3ae",padx=15, pady=5, foreground='red', font=('Ink Free', 25, 'bold'), width=50, height=10)
textArea.pack()

submitButton =  Button(root, text="Submit", width=10, height=2,command=display,foreground='white', border=2, background="#0ca2b6")
submitButton.pack()

root.mainloop()
