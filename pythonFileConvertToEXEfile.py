# Method 1.
# To convert .py file to .exe, we will first install pyinstaller in terminal. command:(pip install pyinstaller)
# then run another command in terminal. command( pyinstaller --onefile --window FileName.py)


# Method 2.
# To convert .py file to .exe, we will first install cx-Freeze in terminal. command:(pip install cx-Freeze)
# then create another python file with any name (e.g script.py, build.py)
# paste this code into that file.
# Code:
# from cx-Freeze import setup, Executable
# setup(
#     name = "YourAppName"
#     version = "1.0"
#     description = "My First App "
#     executables = [Executable("PythonFileName.py")]
# )

# Now save the file and run it through terminal with this command.
# python build.py build


# Make Installer APK of .exe file
'''
Now if you want to make installer apk of the .exe file which you have created erlier.
for this goto brwser and search "inno setup"  and dwonload there app.
and install the app, after installtion open the app, click on file, click on new.
give name of your apk and other details and click next.
now select the .exe file that you have created and go next fill the details at last you will have your own apk installer.

'''