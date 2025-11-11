from tkinter import *
from tkinter import messagebox #import message box library


root = Tk()
root.title("Messagebox Buttons")
root.geometry("300x450")
def clicked():
    messagebox.showinfo(title="Professor.", message="Hello Professor.")

def WarnClicked():
    messagebox.showwarning(title="Warning",icon='warning', message="warning! Don't Click last Button.")

def submitClicked():
   if messagebox.askokcancel(title="Ask OK", message="Do you want to submit it."):
       print("You Submit it")
   else:
       print("You are not submiting yet.")

def QuestionClicked():
   answer = messagebox.askquestion(title="Agree/Disagree", message="Are you Agree?")
   print(answer)
   if answer=="yes":
       print("I agree")
   else:
       print("I am not Agree")

def yesNoCancelClicked():
   answer = messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like coding?")
   print(answer)
   if answer==True:
       print("I like coding")
   elif answer==False:
       print("I don't like code")
   else:
       print("I don't know Coding")

def retryClicked():
   if messagebox.askretrycancel(title="Try again", message="Try Again!"):
       print("Sorry.")
   else:
       print("No I am not confirming it.")

def errorClicked():
    # while(True):
    messagebox.showerror(title="Virus Appeard.", message="Virus!!!")

submitbuton = Button(root, text="Submit", command=submitClicked, width=12, height=2, background="green", foreground='white', border=2, font=("Arial", 12))
submitbuton.pack(pady=5)
submitbuton = Button(root, text="Like?", command=yesNoCancelClicked, width=12, height=2, background="magenta", foreground='white', border=2, font=("Arial", 12))
submitbuton.pack(pady=5)

retrybuton = Button(root, text="Confirm", command=retryClicked, width=12, height=2, background="cyan", foreground='white', border=2, font=("Arial", 12))
retrybuton.pack(pady=5)

askQuestionbuton = Button(root, text="Question", command=QuestionClicked, width=12, height=2, background="black", foreground='white', border=2, font=("Arial", 12))
askQuestionbuton.pack(pady=5)

buton = Button(root, text="Click me", command=clicked, width=12, height=2, background="#0077AF", foreground='white', border=2, font=("Arial", 12))
buton.pack(pady=5)

Warningbuton = Button(root, text="Warning", command=WarnClicked, width=12, height=2, background='yellow', foreground='red', border=2, font=("Arial", 12))
Warningbuton.pack(pady=5)

erorbuton = Button(root, text="Don't Click me", command=errorClicked, width=12, height=2, background='red', foreground='white', border=2, font=("Arial", 12))
erorbuton.pack(pady=5)


root.mainloop()