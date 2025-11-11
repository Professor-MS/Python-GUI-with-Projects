from tkinter import *
root = Tk()

root.title("Check Button")
root.geometry('500x500')

icon = PhotoImage(file='deepseek.png')
root.iconphoto(True, icon)

def Display_1():
    if x_1.get()==1:
        print("Yes! I Agree.")
    else:
        print("No! I am not Agree.")

def Display_2():
    if x_2.get()==True:
        print("Yes! I Agree.")
    else:
        print("No! I am not Agree.")

def Display_3():
    if x_3.get()=="Yes":
        print("Yes! I Agree.")
    else:
        print("No! I am not Agree.")


x_1 = IntVar()
x_2= BooleanVar()
x_3 = StringVar()
check_1 = Checkbutton(root, text="Are you Agree?", variable=x_1, onvalue=1, offvalue=0,command=Display_1, image=icon, compound="right")
check_2 = Checkbutton(root, text="Are you Agree?", variable=x_2, onvalue=True, offvalue=False,command=Display_2, image=icon, compound="right")
check_3 = Checkbutton(root, text="Are you Agree?", variable=x_3, onvalue="Yes", offvalue="No",command=Display_3, image=icon, compound="right")
check_1.pack()
check_2.pack()
check_3.pack()

root.mainloop()


