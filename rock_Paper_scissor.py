import random

ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'


choicesWithValue= {ROCK : 'Rock', SCISSOR : 'Scissor', PAPER : 'Paper'} #dictionary
choices = tuple(choicesWithValue.keys()) #this means tuple ==> choices = (ROCK,SCISSOR,PAPER)
# while True:
#        userChoice = input("Rock, Paper, Scissor. (r,s,p): ").lower()
#        if userChoice not in choices:
#               print("Invalid Choice.")
#               continue
#        computerChoice = random.choice(choices)

#        print(f"You Choose {choicesWithValue[userChoice]}\n Computer Choose {choicesWithValue[computerChoice]}")

#        if userChoice == computerChoice:
#               print("Both have same choices")
#        elif (
#        (userChoice==ROCK and computerChoice == SCISSOR) or 
#        (userChoice==SCISSOR and computerChoice==PAPER) or  
#        (userChoice==PAPER and computerChoice==SCISSOR)):
#               print("You Win.")
#        else:
#               print("You Lose")

#        should_Continue = input("Continue? (y/n): ").lower()
#        if should_Continue=='n':
#               break



# Implementation of the above code through function
def choice():
    while True:
       userChoice = input("Rock, Paper, Scissor. (r,s,p): ").lower()
       if userChoice in choices:
              return userChoice
       else:
              print("Invalid Choice.")

def displayChoice(userChoice, computerChoice):
       print(f"You Choose {choicesWithValue[userChoice]}\n Computer Choose {choicesWithValue[computerChoice]}")

def winner(userChoice, computerChoice):
       if userChoice == computerChoice:
             print("Wow! you both same choices")
       elif (
       (userChoice==ROCK and computerChoice == SCISSOR) or 
       (userChoice==SCISSOR and computerChoice==PAPER) or  
       (userChoice==PAPER and computerChoice==SCISSOR)):
              print("You Win.")
       else:
             print("You Lose.")

def playGame ():
      while True:
       userChoice = choice()
       computerChoice = random.choice(choices)
       displayChoice(userChoice, computerChoice)
       winner(userChoice, computerChoice)
       should_Continue = input("Continue? (y/n): ").lower()
       if should_Continue=='n':
              break

playGame()