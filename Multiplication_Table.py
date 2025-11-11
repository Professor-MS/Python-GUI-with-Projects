from tkinter import *

root = Tk()
root.title("Table")
root.geometry("400x600")
root.config(background="#eff59e")
# Function to calulate Multiplication Table of enterd number.
def Calculate():
    resultLabel.config(text="", bg='#eff59e')
    try:
        resultText = ""
        num = int(entryNum.get())
        for i in range(1,16):
            resultText += f"{i} X {num} = {i*num}\n"
        resultLabel.config(text=resultText, bg='#eff59e')
    except ValueError:
        resultLabel.config(text="Please Enter Valid Number", fg='red')

# Entry
entryNum = Entry(root, font=("Times New Roman", 12, 'bold'))
entryNum.pack(pady=15)
# Button
SubmitButton = Button(root, text='Find', font=("Helvetica", 14, 'bold'), width=10, border=2, command=Calculate )
SubmitButton.pack(pady=10)
# Result Output
resultLabel = Label(root, text='', font=("Ink Free", 16, "bold"), bg='#eff59e')
resultLabel.pack()

root.mainloop()