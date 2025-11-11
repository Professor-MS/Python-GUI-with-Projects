from tkinter import *
from time import *

root = Tk()
root.geometry("400x300")

root.config(background="#ffeeaa")
def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d, %Y")
    dateLabel.config(text=dateString)

    root.after(1000, update) #refresh or update window after each 1 millisecond

timeLabel = Label(root, font=("Impact", 35),pady=20, fg="#0026ff", bg="#ffeeaa")
timeLabel.pack()

dayLabel = Label(root, font=("Times New Roman", 25), fg="#0026ff", bg="#ffeeaa")
dayLabel.pack()

dateLabel = Label(root, font=("Times New Roman", 45, 'bold'), fg="#0026ff", bg="#ffeeaa")
dateLabel.pack()

update()
root.mainloop()