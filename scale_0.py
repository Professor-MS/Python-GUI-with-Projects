from tkinter import *

root = Tk()
root.title("Scale")
root.geometry('200x650')

flamImg = PhotoImage(file="flame.png")
flamlabel = Label(root, image=flamImg)
flamlabel.pack()
coldImg = PhotoImage(file="cold.png")
coldlabel = Label(root, image=coldImg)

def temprature():
    temper = tempraturScale.get()
    print(f"\nTemprature is {temper} degrees C")
    if temper<=20 and temper>= 0:
        print("it's Cold Weather.")
    elif temper<=35 and temper>= 20:
        print("it's Normal Weather.")
    elif temper<=60 and temper>= 35:
        print("it's hot Weather.")
    elif temper<=80 and temper>= 60:
        print("it's very hot Weather.")
    elif temper<=90 and temper>= 80: 
        print("it's extremely hot Weather.")
    elif temper<=100 and temper>= 90:
        print("it's extremely hot Weather. Reach to Boilling point")
    else:
        print("huhuhh! Enjoye")

tempraturScale = Scale(root, from_=100, to=0, font=("Consolas", 16), tickinterval=10, background='black', foreground='#00f000',sliderlength=20, troughcolor="#5AFF45", showvalue=0,length=400,width=30, orient='vertical')
tempraturScale.pack(pady=10)
coldlabel.pack()

submitButton = Button(root, text="Submit", command=temprature, border=3, width=15, height=3)
submitButton.pack(pady=10)



root.mainloop()