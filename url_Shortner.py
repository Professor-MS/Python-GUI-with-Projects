import pyshorteners
import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("System")   #Dark  Light  System
ctk.set_default_color_theme("dark-blue")   # blue  green

root = ctk.CTk()
root.geometry('400x300')
root.title("URL Shortner App")

def shortUrl():
     link = LinkEntry.get()
     shortener = pyshorteners.Shortener()
     shortend_link = shortener.tinyurl.short(link)
     print("Shortend URL: ",shortend_link)

linkLabel = ctk.CTkLabel(root, text="Enter Your Link ")
LinkEntry = ctk.CTkEntry(root)

shortenButton = ctk.CTkButton(root, text='Shorten URL' ,command=shortUrl)

linkLabel.pack(pady=10)
LinkEntry.pack(pady=10)
shortenButton.pack(pady=10)
root.mainloop()
