from tkinter import *

# grid is a geometry manager that organizes widget in a table-like structure.
root = Tk()
root.title("Grid Layout")
root.geometry('400x400')


def personal_Info():
    window = Toplevel()
    window.geometry('500x300')
    nam = (firstEntry.get()+" "+Lastentry.get())
    emai = emailEntry.get()
    namlab = Label(window, text=nam, font=("Impact", 24, 'bold'))
    namlab.pack()
    emaillab = Label(window, text=emai, font=("Times New Roman", 22, 'bold'))
    emaillab.pack()
    print(f"Name: {nam}\n Email: {emai}")


Label(root, text="Personal Info", font=("Helvetica rounded", 28, 'bold')).grid(row=0, column=1, pady=20)
firstName = Label(root, text="First Name", font=("Monotype corsiva", 18))
firstName.grid(row=1, column=0)
firstEntry = Entry(root, width=20, font=('Mistral', 18))
firstEntry.grid(row=1,column=1, columnspan=3)

lastName = Label(root, text="Last Name", font=("Monotype corsiva", 18))
lastName.grid(row=2, column=0)
Lastentry = Entry(root, width=20, font=('Mistral', 18))
Lastentry.grid(row=2,column=1, columnspan=3)

email = Label(root, text="Email", font=("Monotype corsiva", 18))
email.grid(row=3, column=0)
emailEntry = Entry(root, width=20, font=('Helvetica Rounded', 16))
emailEntry.grid(row=3,column=1, columnspan=3)


bt_1 = Button(root, text="Submit",font=("Segoe script", 14), width=15, height=2, command=personal_Info)
bt_1.grid(row=4, column=1, columnspan=2, pady=20)

root.mainloop()