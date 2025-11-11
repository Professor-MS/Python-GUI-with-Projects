# import tkinter as ttk
from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator")
root.geometry('400x200')
root.config(background="#9cc1e5")

def ShortURL():
    url =URL_Entry.get().strip()
    filename = filename_Entry.get().strip()
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    image = qr.make_image(fill_color= 'black', back_color = 'white')
    image.save(filename)
    Message(root, text=f"File Saved in the name {filename}").grid(row=3,column=0, columnspan=2)


url_label = Label(root, text="Enter URL here", background="#9cc1e5")
url_label.grid(row=0, column=0,padx=10,)

URL_Entry = Entry(root,)
URL_Entry.grid(row=0,column=1, pady=15)

filename_label = Label(root, text="Enter file name", background="#9cc1e5")
filename_label.grid(row=1, column=0, padx=10, pady=10)

filename_Entry = Entry(root)
filename_Entry.grid(row=1, column=1, pady=15)

url_shorten_button = Button(root, text= "Shorten Link", command=ShortURL)
url_shorten_button.grid(row=2,column=1, pady=15)

root.mainloop()

# import qrcode
# data = input("Enter the text or URL : ").strip()
# fileName = input("Enter the File Name: ").strip()

# qr = qrcode.QRCode(box_size=10, border=4)
# qr.add_data(data)

# image = qr.make_image(fill_color= 'black', back_color = 'white')
# image.save(fileName)
# print(f"QR Code save as {fileName}")