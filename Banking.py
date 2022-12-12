# This is a basic Python program for a banking app

# Define a dictionary to store the user's bank account information
bank_account = {}

# Define a function to display the user's bank account information
def display_account_info():
    print(f"Account balance: {bank_account['balance']}")

# Define a function to allow the user to deposit money into their account
def deposit(amount):
    # Add the deposit amount to the user's account balance
    bank_account['balance'] += amount
    print(f"Successfully deposited {amount} into your account.")

# Define a function to allow the user to withdraw money from their account
def withdraw(amount):
    # Check if the user has sufficient funds in their account
    if bank_account['balance'] >= amount:
        # Deduct the withdrawal amount from the user's account balance
        bank_account['balance'] -= amount
        print(f"Successfully withdrew {amount} from your account.")
    else:
        print("Insufficient funds in your account.")

# Define a function to allow the user to check their account balance
def check_balance():
    print(f"Your account balance is {bank_account['balance']}.")

# Initialize the user's bank account with a starting balance of 0
bank_account['balance'] = 0

# Allow the user to perform various banking operations
while True:
    # Prompt the user to select an operation
    print("Select an operation:")
    print("1. Display account info")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Quit")
    operation = input("Enter the number of the operation you want to perform: ")

    # Perform the selected operation
    if operation == '1':
        display_account_info()
    elif operation == '2':
        amount = int(input("Enter the amount you want to deposit: "))
        deposit(amount)
    elif operation == '3':
        amount = int(input("Enter the amount you want to withdraw: "))
        withdraw(amount)
    elif operation == '4':
        check_balance()
    elif operation == '5':
        break
    else:
        print("Invalid operation. Please try again.")

