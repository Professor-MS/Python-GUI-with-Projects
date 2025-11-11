from tkinter import *

root = Tk()
root.title("Button")
root.geometry("400x400")

icon = PhotoImage(file="youtube.png")
root.iconphoto(True, icon)

count= 0
def buttonClick():
    global count
    count+=1
    print(f"Subscribe Done {count}, time")

    
Subscribe = Button(root, text="Subscribe Now", background='black', foreground='white', padx=15, pady=10, command= buttonClick, font=("Comic Sans", 20, "bold"), border=10, activebackground="#114b11", activeforeground='yellow', state="active", image=icon, compound='bottom')
Subscribe.pack()


root.mainloop()