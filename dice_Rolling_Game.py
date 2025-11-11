import random
while True:
    message = input("Roll the dice? y/n ").lower()
    if message == "y":
        num1 = random.randint(1,6)
        num2 = random.randint(6,12)
        print(f"\n\tDice: [{num1}], [{num2}]\n")
    elif message == "n":
        print("Thanks for playing game.")
        break
    else:
        print("Invalid Choice.")


# count = 0
# numOfDice = int(input("How many dice you want to rolle: "))
# playing = True
# while playing: 
#     message = input("Roll the dice? y/n ").lower()
#     if message == "y":
#         for x in range(numOfDice):
#             num1 = random.randint(1,6)
#             num2 = random.randint(6,12)
#             print(f"\n\tDice: [{num1}], [{num2}]\n")
#             count+=1
#     elif message == "n":
#         print("Thanks for playing game.")
#         playing=False
#     else:
#         print("Invalid Choice.")

# print(f"\nYou roll the dice {count} times")

