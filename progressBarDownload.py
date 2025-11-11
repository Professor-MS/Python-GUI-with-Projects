from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

root.geometry("500x200")
root.title("Progress Bar")

def Download():
    task =10
    x= 0
    while (x<task):
        time.sleep(1) #this will delay the operation 1 second
        bar['value']+=10 #incresing bar fill with 10%
        x+=1
        percent.set(str(int((x/task)*100))+"%")
        text.set(str(x)+"/"+str(task)+" task completed")
        root.update_idletasks() #we need to refresh the window after each iteration that the progress should appear 



percent = StringVar()
text = StringVar()
bar = Progressbar(root, length=350)
bar.pack()
taskLabel = Label(root, textvariable=text)
percentLabel = Label(root, textvariable=percent)
percentLabel.pack()
taskLabel.pack()
downloadButton = Button(root, text="Download", command=Download)
downloadButton.pack()


root.mainloop()
