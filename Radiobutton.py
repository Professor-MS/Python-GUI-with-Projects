from tkinter import *

root = Tk()

root.title("RadioButton")
root.geometry("630x500")

def selectedLanguage():
    if x.get()==0:
        print("Great! Your Favourite Language is Python. it's easy to learn. good Choice.\n")
    elif x.get()==1:
        print("Nice! C++ is powerfull Language. it's will build your logic. love that.\n")
    elif x.get()==2:
        print("Wow!  Java is Popular language. it mostly used for Mobile Applications. Awesome.\n")
    elif x.get()==3:
        print("Facinating!  it means you love Scripting Language. JavaScript mostly used in Web Development. Amazing.\n")
    else:
        print("No Problem, you love all\n")

#  Photos of Laguages
languageList = ["Python","C++", "Java", "JavaScript"]
python = PhotoImage(file="Python.png")
cpp = PhotoImage(file="cpp.png")
java = PhotoImage(file="java.png")
javaScript = PhotoImage(file="javaScript.png")
# List of Photos
languageImages = [python, cpp, java, javaScript]
#  Question Label
whichLanguage = Label(root, text="Which one is your Favourite Language?", font=("Helvetica", 20, 'bold'), padx=15)
whichLanguage.pack(side="top")


x = IntVar()
# Loop to display all Radiobuttons
for index in range(len(languageList)):
    chioce = Radiobutton(root, text=languageList[index], variable=x, padx=20, font=("Cascadia Code", 18, 'bold'), value=index, image=languageImages[index], command=selectedLanguage, compound="right")
    chioce.pack(anchor='w')

root.mainloop()