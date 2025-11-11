# List Box: a listing of selectable text items within its own container.
from tkinter import *

root = Tk()

root.title("List Box")
# root.geometry("400x400")

icon = PhotoImage(file="javaScript.png")
root.iconphoto(True, icon)

def Submit():
    # item=listBox.get(listBox.curselection()) #This will select current selected items and catch it
    # print("You Orderd",item)
    food= []
    for index in listBox.curselection():
         food.insert(index, listBox.get(index)) #to order multiple food items
    for i in food:
        print("You orderd",i)

def InsertNewItem():
    ite= NewItem.get()
    listBox.insert(END,ite)
    listBox.config(height=listBox.size()) # Dynamically chnage the Size of container as new item insert

def deleteItem():
    # listBox.delete(listBox.curselection())
    for index in reversed(listBox.curselection()): #Delete multiple items by selecting multiples
        listBox.delete(index)        

    listBox.config(height=listBox.size())

def Clear():
    insertItem.delete(0, END)

listBox = Listbox(root,selectmode='multiple', background="#f7ffde", font=("Constantia", 18), width=20)
listBox.pack()
listBox.insert(1,"Pizza")
listBox.insert(2,"Bread")
listBox.insert(3,"Chicken")
listBox.insert(4,"Baryani")
listBox.insert(5,"Burger")
listBox.insert(6,"Chai")
listBox.config(height=listBox.size())

NewItem = StringVar()

insertItem = Entry(root, background="#3b4421", font=("Constantia", 18),border=5, relief='sunken', foreground='white', textvariable=NewItem)
insertItem.pack()
submitButton = Button(root, text="Submit",width=15, pady=5, command=Submit, font=("Impect", 13,'bold'),border=2,background='blue', foreground='white')
submitButton.pack()
submitButton = Button(root, text="Insert Item",width=15, pady=5, command=InsertNewItem, font=("Impect", 13,'bold'),border=2, background='green', foreground='white')
submitButton.pack()
DeleteButton = Button(root, text="Delete Item",width=15, pady=5, command=deleteItem, font=("Impect", 13,'bold'),border=2, background='red', foreground='white')
DeleteButton.pack()
ClearButton = Button(root, text="Clear",width=15, pady=5, command=Clear, font=("Impect", 13,'bold'),border=2, background='yellow', foreground='red')
ClearButton.pack()


root.mainloop()