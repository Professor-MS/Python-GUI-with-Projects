from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

root.geometry("500x200")
root.title("Progress Bar")

def Download():
    GB =100
    download= 0 
    speed = 1
    while (download<GB):
        time.sleep(0.05) #this will delay the operation 1 second
        bar['value']+=(speed/GB)*100 #incresing bar fill with 10%
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        root.update_idletasks() #we need to refresh the window after each iteration that the progress should appear 



percent = StringVar()
text = StringVar()
bar = Progressbar(root, length=350, orient=HORIZONTAL)
bar.pack()
taskLabel = Label(root, textvariable=text)
percentLabel = Label(root, textvariable=percent)
percentLabel.pack()
taskLabel.pack()
downloadButton = Button(root, text="Download", command=Download)
downloadButton.pack()


root.mainloop()
