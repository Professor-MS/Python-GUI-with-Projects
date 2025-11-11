import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x500')
root.title("Image import 2nd method")

# Load image
imagePath = "ProfilePic.jpg"
MyImage = Image.open(imagePath)

# Resize Image
# resizedImage = img.resize((200,300))

# Display Image
tk_image = ImageTk.PhotoImage(MyImage)
# tk_image = ImageTk.PhotoImage(resizedImage)

# Pack Image
label_1 = ttk.Label(root, image=tk_image)
label_1.pack()


root.mainloop()