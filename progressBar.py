import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x500')
window.title("Progrss Bar")

progressBar = ttk.Progressbar(window, length=300, orient='horizontal', mode="determinate", value=10,maximum=120,)
# progressBar = ttk.Progressbar(window, length=300, orient='vertical', mode="determinate", value=10,maximum=120,)
# progressBar = ttk.Progressbar(window, length=300, orient='horizontal', mode="indeterminate")

DownloadButton = ttk.Button(window,text="Download",command= lambda: progressBar.start())
stopButton = ttk.Button(window,text="Stop",command= lambda: progressBar.stop())
progressBar.pack()
DownloadButton.pack()
stopButton.pack()

window.mainloop()