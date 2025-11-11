import random 
number = random.randint(1, 50)
while True:
    try:
        userNumber = int(input("Guess the number (1-50): "))
        if userNumber<1 or userNumber>50:
            print("\n\t*****Choose number between 1 - 50  ****\n")
        elif userNumber==number:
            print("\n\tWow! You Guess the number.\n")
            break
        elif userNumber<number:
            print("Too Low")
        elif userNumber>number:
            print("Too High.")
        else:
            print("Not Valid.")
    except ValueError:
        print("Please enter a valid Number.")
        
