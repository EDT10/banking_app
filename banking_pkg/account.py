def show_balance(balance):
    print("---")
    print(f"Your current balance is: ${balance}")


def deposit(balance):
    print("---")
    amount = float(input("Enter amount to deposit: "))
    return float(balance) + float(amount)



def withdraw(balance):
    print("---")
    amount = float(input("Enter amount to withdraw: "))
        
    return float(balance) - float(amount)


def logout(name):
    print("---")
    print(f"Goodbye {name}")


