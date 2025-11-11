import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Tree view")

table = ttk.Treeview(window, columns=("Name","category","Product_Price"), show="headings tree")


table.heading("Name", text="Product", anchor='w')
table.heading("category", text="Category",anchor='w')
table.heading("Product_Price", text="Price",anchor='w')

table.insert(parent="", iid='Iphone',index=0, values=("iPhone","Electronics","500$"))
table.insert(parent="", iid='Andphone',index=1, values=("Samsung","Electronics","450$"))
table.insert(parent="", iid='airpod',index=2, values=("AirPods","Gadgets","50$"))
table.insert(parent="", iid='vehical',index=3, values=("Car","Vehical","8000$"))
table.insert(parent="", iid='Laptop',index=4, values=("Laptop","Electronics","600$"))

table.insert(parent="", iid='Tshirt',index='end', values=("T-shirt","Fashion","200$"))


table.insert(parent="Iphone", iid='iphone12',index='end', values=("IPhone 12","Apple","430$"))
table.insert(parent="Iphone", iid='iphone13',index='end', values=("IPhone 13 Pro","Apple","510$"))
table.insert(parent="Iphone", iid='iphone14',index='end', values=("IPhone 14 Pro Max","Apple","550$"))
table.insert(parent="Andphone", iid='android0',index='end', values=("SAMSUNG S24 Ultra","Android","550$"))
table.insert(parent="Andphone", iid='android1',index='end', values=("SAMSUNG S25 Ultra","Android","650$"))
table.insert(parent="Tshirt", iid='t_shirt',index='end', values=("Jacket","Fashion","250$"))
table.insert(parent="Laptop", iid='delLaptop',index='end', values=("Dell Core i9 12th Gen","Laptop","600$"))
table.insert(parent="Laptop", iid='hpLaptop',index='end', values=("Dell Core i7 10th Gen","Laptop","520$"))
table.insert(parent="vehical", iid='car1',index='end', values=("Corolla XLI","Car","5200$"))
table.insert(parent="vehical", iid='car2',index='end', values=("Vitz","Car","5800$"))
table.insert(parent="vehical", iid='car3',index='end', values=("Prado","Car","8200$"))




table.pack(expand=True, fill='both')
window.mainloop()