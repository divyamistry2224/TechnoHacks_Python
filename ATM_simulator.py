# Task : ATM simulator
# Create a program that simulates the all atm functionalities and operations 
# (Check balance, Deposit, Withdraw)


def deposit(balance):
    amountToDeposit = int(input("Please enter amount to deposit: "))
    balance += amountToDeposit
    print(f"Thank you for depositing, new balance is ₹{balance}")
    return balance

def withdraw(balance):
    amountToWithdraw = int(input("Please enter amount to withdraw: "))
    if amountToWithdraw > balance:
        print("Insufficient funds in your account")
    else:
        balance -= amountToWithdraw
        print(f"You have withdrawn ₹{amountToWithdraw}.00 and your balance is ₹{balance}.00")
    return balance

def check_balance(balance):
    print(f"Your bank amount balance is: ₹{balance}.00")
    

def atm_simulator():
    balance = 0
    pin = "1234"  # Set the PIN
    attempts = 3  # Number of allowed attempts

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN accepted. Access granted.")
            break
        else:
            attempts -= 1
            print(f"Invalid PIN. {attempts} attempt(s) remaining.")
    else:
        print("Too many incorrect attempts. Exiting.")
        return

    while True:
        print("\nEnter any option to be served!\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_simulator()