def show_balance(balance):
    print("Your balance is:$", float(balance))


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return float(balance) + float(amount)

def withdraw(balance):
    amount = float(input("Emnter amount to withdraw"))
    return float(amount) - float(balance)


def logout(name):
    print(f"Goodbye {name}")


