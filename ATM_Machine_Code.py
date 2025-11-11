userName="Professor"
userPass=123
current_balance=10
counter=0
option=0
def logIn():
    global userName
    global userPass
    global counter
    id=input("Enter Username: ")
    passw=int(input("Enter your Password: "))
    if id==userName and passw==userPass:
        print("__Welcome To ATM Machine__")
        homePage()
    else:
        print("Wrong Username or Password...\nTry Again")
        counter+=1
        while counter<3:
            logIn()
        else:
            print("Account Suspended...")


def homePage():
    global option
    global current_balance
    print("\t1. Check Balance\n\t2. Withdraw\n\t3. Deposit\n\t4. Exit")
    option=int(input("Enter from the above Options: "))
    while option==1 or option==2 or option==3 :
        print("\t1. Check Balance\n\t2. Withdraw\n\t3. Deposit\n\t4. Exit")
        option=int(input("Enter from the above Options: "))
        if option==1:
            print(f"\n\t==>Your Current Balance: {current_balance}$\n")
        elif option==2:
            withdraw=int(input("Enter withdraw Amount: "))
            if withdraw>current_balance:
                print("\n\t==>Insufficient Balance.\n")            
            else:
                checkpas=int(input("Enter Password: "))
                if checkpas==userPass:
                    print("\n\t==>",withdraw,"$ Withdraw Succesful.\n")
                    current_balance=current_balance-withdraw
                    print(f"\n\t==>Your Current Balance: {current_balance}$\n")

                else:
                    print("Wrong Password...")
        elif option==3:
            deposit=int(input("Enter Deposit Amount: "))
            current_balance=current_balance+deposit
            print(f"\n\t==>Your Current Balance: {current_balance}$\n")
        else:
            print("Thanks for Using Our Services.\nHave a Nice Day",userName)
logIn()