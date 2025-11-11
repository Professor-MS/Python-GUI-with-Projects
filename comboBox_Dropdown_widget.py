import tkinter as tk
from tkinter import ttk

Root = tk.Tk()
Root.geometry('400x300')
Root.title("Combo-box or Drop-down")
countryList = ("Pakistan", "Russia", "Iran", "Japan", "india", "China", "Australia", "Turky", "Palestine", "Afghanistan", "Bangladesh")
label_1 =ttk.Label(Root, text="Country")

# selectedCountry = tk.StringVar(value="Pakistan")   #By Default Value is Pakistan.
selectedCountry = tk.StringVar(value=countryList[0])  #here By Default Value will be those which is at index no: 0.

countryName = ttk.Combobox(Root, textvariable=selectedCountry)
countryName["values"] = countryList
bt_1 = ttk.Button(Root, text="Show Value", command= lambda: print(selectedCountry.get()))

label_1.pack()
countryName.pack(pady=10)
bt_1.pack()


Root.mainloop()