import random
Number = random.randint(1,10)
for i in range(3):
    userNumber = int(input("Guess the Number (1 - 10): "))
    if userNumber == Number:
        print("WOW! You guessed the number right, it's ",Number)
        break
    else:
        print("Wrong guess. Try again! ")

if userNumber != Number:
    print("Sorry! You used all attempts. The number was ",Number)