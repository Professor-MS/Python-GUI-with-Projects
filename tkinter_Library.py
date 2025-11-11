import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
MainWindow = tk.Tk()
# MainWindow = ttk.Window(themename="darkly")
MainWindow.geometry("600x300")

MainWindow.title("Distance Convertor")
# main Window
# Widget
# style
# Layout
# pack

# Functions
def calculate():
        inData = inputVar.get()
        metToKiloMeter = inData/1000
        outputVar.set(metToKiloMeter)

# frame
frame_1 = ttk.Frame(MainWindow)

# Widgets
inputVar = tk.IntVar()
label_1 = ttk.Label(master=MainWindow, text='Meter to Kilo-meter Convertor', font='helvetica 20 bold')
inputSection = ttk.Entry(frame_1, textvariable=inputVar)
button = ttk.Button(frame_1, text='Convert',command=calculate)
label_2 = ttk.Label(frame_1)
outputVar = tk.StringVar(value="")

# outputLabel = ttk.Label(MainWindow, text="Calulated Value: ")
output = ttk.Label(MainWindow, textvariable=outputVar, font=("Times New Roman", 30, 'bold'))
# packing
label_1.pack()
inputSection.pack(fill='both',side='left')
button.pack(fill='both',side='left')
label_2.pack()
frame_1.pack()
# outputLabel.pack()
output.pack(pady=30)

MainWindow.mainloop()