# Miles to Kilometer Convertor
from tkinter import *
# import ttkbootstrap as ttk #to Install this module (pip install ttkbootstrap)
root = Tk()
# root = ttk.window(themname = 'darkly') # 'darkly' or 'journal
root.title("Miles to Kilometer Convertor")
root.geometry("500x300")

# function for calculation
def Convert():
    mileIpnput = inputVariable.get()
    km_Output = (mileIpnput * 1600)/1000
    # km_Output = mileIpnput * 1.61
    outPutString.set(str(km_Output)+" Kilometer")


lab = Label(root, text="Miles to Kilometers", font=("Helvetica", 20, 'bold'))
lab.pack()

# input
inputVariable = IntVar()
frame = Frame(root)
entryBox = Entry(frame,textvariable=inputVariable,font=("Georgia",18))
but = Button(frame, text='Convert', font=('Ink Free', 14, 'bold'), background="#ad3973", foreground='white', command= Convert)
entryBox.pack(pady=20,side= 'left')
but.pack(pady=8, padx=8,side='left')
frame.pack()

# output
outPutString = StringVar()
value = Label(root, text='Output here', textvariable=outPutString, font=('Ink Free', 14, 'bold') )
value.pack()

root.mainloop()