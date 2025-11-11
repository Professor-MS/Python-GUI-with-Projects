import tkinter as tk
import customtkinter as ctk
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.minsize(400, 500)
root.maxsize(450, 550)
root.title("Sign Up...")

def SignUpDetail():
    name = NameEntry.get()
    PhoneNum = mobileNoEntry.get()
    country = countryVar.get()
    gender = optionVariable.get()
    email = EmailEntry.get()
    passw = PasswordEntry.get()
    with open("signup_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        # Optional: Write header once
        if file.tell() == 0:
            writer.writerow(["Name", "Mobile", "Country", "Gender", "Email", "Password"])
        writer.writerow([name, PhoneNum, country, gender, email, passw])


    # Clear the existing Widget
    for widget in root.winfo_children():
        widget.destroy()

    # Profile in the same window
    ProfileLabel = ctk.CTkLabel(root, text="Profile", font=("Helvetica", 22, "bold"))
    ProfileLabel.pack(pady= 15)

    profileText=f"""Name: {name}\nMobile No: {PhoneNum}\nCountry: {country}\nGender: {gender}\nEmail: {email}\nPassword: {passw}"""
    ProfileDetail = ctk.CTkLabel(root,text= profileText, font=("Helvetica", 14, "bold"), justify="left")
    ProfileDetail.pack(pady=10)
   

# Sign Up Label 
signUpLabel = ctk.CTkLabel(root, text="Sign Up", font=("Helvetica", 20, "bold"))

# Name
NameLabel = ctk.CTkLabel(root, text="Name")
NameEntry = ctk.CTkEntry(root, width=200, placeholder_text="Name")

# Mobile Number
MobileNoLabel = ctk.CTkLabel(root, text="Mobile No")
mobileNoEntry = ctk.CTkEntry(root, width=200)

# Country Selection
countryList = ("Pakistan", "Russia", "Iran", "Japan", "india", "China", "Australia", "Turky", "Palestine", "Afghanistan", "Bangladesh")
countryVar = ctk.StringVar(value=countryList[0])

countryLabel = ctk.CTkLabel(root, text="Country")
countrySelection = ctk.CTkComboBox(root, values=countryList, variable=countryVar)

# Gender Selection
optionVariable = tk.StringVar()
genderLabel = ctk.CTkLabel(root, text="Gender")
male = ctk.CTkRadioButton(root, text="Male", variable=optionVariable, value='Male')
female = ctk.CTkRadioButton(root, text="Female", variable=optionVariable, value='Female')

# Email
EmailLabel = ctk.CTkLabel(root, text="Email")
EmailEntry = ctk.CTkEntry(root)

# Password
PasswordLabel = ctk.CTkLabel(root, text="Password")
PasswordEntry = ctk.CTkEntry(root, show='*')

# Sign Up Button 
signUpButton = ctk.CTkButton(root, text="Sign Up", command=SignUpDetail)



# _____________ Placing Widget ____________________
signUpLabel.place(relx=0.43, rely=0.1)

NameLabel.place(relx=0.1, rely=0.2)
NameEntry.place(relx=0.28, rely=0.2,relwidth=0.5, relheight=0.06)

MobileNoLabel.place(relx= 0.098, rely=0.3)
mobileNoEntry.place(relx=0.28, rely=0.3,relwidth=0.5, relheight=0.06)

countryLabel.place(relx=0.1, rely= 0.4)
countrySelection.place(relx= 0.28, rely= 0.4, relwidth= 0.5, relheight =0.06)

genderLabel.place(relx=0.1, rely= 0.4)
genderLabel.place(relx= 0.1, rely= 0.5)
male.place(relx=0.29, rely= 0.51)
female.place(relx=0.5, rely= 0.51)

EmailLabel.place(relx= 0.1, rely= 0.6)
EmailEntry.place(relx= 0.28, rely= 0.6, relwidth=0.5, relheight=0.06)

PasswordLabel.place(relx= 0.1, rely= 0.7)
PasswordEntry.place(relx= 0.28, rely= 0.7, relwidth=0.5, relheight=0.06)

signUpButton.place(relx= 0.37, rely= 0.8, relwidth=0.3, relheight= 0.09)






root.mainloop()