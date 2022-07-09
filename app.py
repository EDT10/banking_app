from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#Task 2: Registration
print("     === Automated Teller Machine ===    ")
name = input("Enter name to register: ")
pin = int(input("Enter PIN: "))
balance = float(0)

print(f"{name} has been registered with starting balance of ${balance}")
#print(name, "has been registered with starting balance of" + str(balance) )


while True:
    print("LOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = int(input("Enter PIN:"))

    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credential")
        continue

while True:
    atm_menu(name)
    option = int(input("Choose an option: "))
    if option == 1:
        account.show_balance(balance)
        continue
    elif option == 2:
        balance = account.deposit(balance)
        account.show_balance(balance)
        continue
        #print(current_bal)
    elif option == 3:
        balance = account.withdraw(balance)
        current_bal = account.withdraw(balance)
        print("")
        continue
    elif option == 4:
        account.logout(name)
        break
    else:
        print("Invalid opion")
        continue
    



#Task 3: Log in and prompt for menu option



