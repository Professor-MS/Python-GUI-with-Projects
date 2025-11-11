from tkinter import *

root = Tk()
root.title("Entry")
root.geometry('800x400')
root.config(background="#AB0000")

# Logo
icon = PhotoImage(file='Python.png')
root.iconphoto(True, icon)

# Display Function
down =0
def display():
    global down
    down+=115
    txt = inputText.get()
    labl = Label(root, text=f"Hi Hacker! {txt}",font=('Cascadia Code', 22, 'bold'), foreground="#37ff00", background='#AB0000')
    labl.place(x=30, y=down)
    # entry.config(state="disabled")
    # entry.config(show="*")
    

def clear():
    entry.delete(0, END)

def Backspace():
    entry.delete(len(entry.get())-1,END)

inputText = StringVar()
#  Label
label = Label(root, text="Enter your Name", font=('Cascadia Code', 18, 'bold'), foreground='yellow', background='#AB0000')
label.place(x=25, y=5)
#  Entry Box
entry = Entry(root, font=('Cascadia Code', 20, 'bold'), foreground="#00ff00", background="black", textvariable= inputText, border=12, relief='sunken' )
entry.place(x=25, y=50)
# Button
greetButon = Button(root, text="Greet Me", font=('Cascadia Code', 16, 'bold'), foreground="#00ff00", background="black", command= display, border=8, relief='raised')
greetButon.place(x=380, y=50)

ClearButon = Button(root, text="Clear", font=('Cascadia Code', 16, 'bold'), foreground="#00ff00", background="black", command= clear, border=8, relief='raised')
ClearButon.place(x=518, y=50)

backspaceButon = Button(root, text="Backspace", font=('Cascadia Code', 16, 'bold'), foreground="#00ff00", background="black", command= Backspace, border=8, relief='raised')
backspaceButon.place(x=620, y=50)


root.mainloop()