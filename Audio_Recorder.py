import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from scipy.io.wavfile import write
fs = 44100

def RecordingAudio():
    second = inputVar.get()
    recordVoice = sd.rec(int(second*fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    write("Your_Audio.wav", fs, recordVoice)



mainWindow = tk.Tk()
mainWindow.title("Audio Recorder")
mainWindow.geometry("500x300")

inputVar = tk.IntVar()
Seconds = ttk.Label(mainWindow, text="Enter Time Durations in seconds: ")
Secondsinput = ttk.Entry(mainWindow, textvariable=inputVar)
recordingButton = ttk.Button(mainWindow, text="Start Recording",command=RecordingAudio)
outPutLabel = ttk.Label(mainWindow, text="Please check out 'Your_Audio.wav'")
Seconds.pack()
Secondsinput.pack()
recordingButton.pack(pady=30)
mainWindow.mainloop()