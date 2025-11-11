import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Menue ")

# Create Menue Barthrough tk not ttk

menuBar = tk.Menu(window)
window.config(menu= menuBar)

# File Menue
file0 = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="File", menu=file0)

file0.add_command(label="New File", command= lambda: print("New File"))
file0.add_command(label="Open File", command= lambda: print("Open File"))
file0.add_command(label="Save as", command= lambda: print("Save as"))
file0.add_separator()
file0.add_command(label="Export", command= lambda: print("Export"))
file0.add_command(label="Exit", command= lambda: print("Exit"))

# Home Menue

file1 = tk.Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Home", menu=file1)

file1.add_command(label="Audio", command= lambda: print("Audio"))
file1.add_command(label="Video", command= lambda: print("Video"))
file1.add_command(label="Convert Video to MP3", command= lambda: print("Convert Video to MP3"))
file1.add_command(label="Open Camera", command= lambda: print("Open Camera"))

# Edit Menue

file2 = tk.Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Edit", menu=file2)

file2.add_command(label="Trim", command= lambda: print("Trim Audio"))
file2.add_command(label="Crop", command= lambda: print("Crop Video"))
file2.add_command(label="Adjustment", command= lambda: print("Adjustment"))
file2.add_command(label="Scale", command= lambda: print("Scale"))
file2.add_command(label="Position", command= lambda: print("Position"))
file2.add_separator()
file2.add_command(label="Copy (Ctrl+C)", command= lambda: print("Copy"))
file2.add_command(label="Paste (Ctrl+V)", command= lambda: print("Paste"))

window.mainloop()