import random
passLength = int(input("Enter the lenght of password: "))
CharacterSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?><"
randomPassword = "".join(random.sample(CharacterSet, passLength))
print("Generated Password: ",randomPassword,"\nFinish..")
