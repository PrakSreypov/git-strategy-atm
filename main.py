import os

users = {
    "user1": {"password": "1234", "balance": 1000, 'Loan': 0},
    "user2": {"password": "5678", "balance": 2000, 'Loan': 0}
}
current_user = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

def sign_up():
    global users
    print("---- create an account ----")
    username = input("name: ")
    if username in users:
        print("Username already exists. Please choose another username.")
        return
    password = input("Set password: ")
    phone = input("Phone Number:")
    address =  input("Address:")
    #balance = float(input("Enter initial balance: "))
    users[username] = {"password": password, "balance": 0, 'Loan': 0}
    current_user = username
    clear()
    print("Account created successfuly.")
    print()

def sign_in():
    global current_user, users

    print("    ---- Sign in ----") 
    while True :
        username = input("Please Enter your Username: ")
        password = input("Enter Password: ")
        print()
        if username in users and users[username]["password"] == password:
            current_user = username
            clear()
            print(f"Welcome  {username}  ")
            break
                
        else:
            clear()
            print("Invalid user name or password")
            print("---Please reenter again---")
            print("==========================")
            print()



def transfer():
    global users, current_user
    if current_user:
        recipient = input("Enter recipient's username: ")
        if recipient in users:
            amount = float(input("Enter amount to transfer: "))
            if amount <= users[current_user]['balance']:
                clear()
                users[current_user]['balance'] -= amount
                users[recipient]['balance'] += amount
                print(f"Transferred ${amount} to {recipient} successfully.")
            else:
                clear()
                print("Insufficient funds.")
        else:
            clear()
            print("Recipient not found.")
    else:
        clear()
        print("Please sign in to transfer money.")

def withdraw():
    global users, current_user
    if current_user:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            clear()
            print(f"Withdrew ${amount} successfully. New balance: ${users[current_user]['balance']}")
    else:
        clear()
        print("Please sign in first.")

# B Bonthong 
def check_balance():
    global users, current_user
    if current_user:
        clear()
        print(f"Your balance is: {users[current_user]['balance']}")
        loan = users[current_user]["Loan"]
        print(f"Your current Loan is: ${loan}")
    else:
        clear()
        print("Please sign in first.")



def deposit():
    global users, current_user
    if current_user:
        clear()
        amount = float(input("Enter amount to deposit: "))
        users[current_user]['balance'] += amount
        print(f"Deposited ${amount}. New balance: ${users[current_user]['balance']}")
    else:
        clear()
        print("Please sign in first.")




def payment():
    if current_user:
        recipient = input("Enter payment recipient: ")
        amount = float(input("Enter payment amount: "))
        if amount <= users[current_user]["balance"]:
            users[current_user]["balance"] -= amount
            clear()
            print(f"Payment of this ${amount} to {recipient} successful.")
        else:
            clear()
            print("Insufficient funds.")
    else:
        clear()
        print("Please sign in to make a payment.")

def loan():
    if current_user:
        amount = float(input("Enter loan amount: "))
        users[current_user]["balance"] += amount
        users[current_user]["Loan"] += amount
        loan = users[current_user]["Loan"]
        print(f"Loan of ${loan} credited to your account. New balance: ${users[current_user]['balance']}")
    else:
        clear()
        print("Please sign in to apply for a loan.")
        
def payback():
    if users[current_user]['balance'] >= users[current_user]['Loan']:
        users[current_user]['balance'] -= users[current_user]['Loan']
        users[current_user]['Loan'] -= users[current_user]['Loan']
        clear()
        print('Congrat now you release from laon')
    else:
        clear()
        print('ypu do not have enought money to buy food')

def profile():
    global users, current_user
    if current_user:
        clear()
        print(f"Balance: ${users[current_user]['balance']}")
        print(f"Loan needed to pay: ${users[current_user]['Loan']}")
    else:
        print("Please sign in first.")




# # B Bunthong 
def display():
    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Check Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Payment")
        print("8. Loan")
        print("9. Profile")
        print('10. Pay back loan to bank')
        print("11. Logout")
        print("12. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            sign_up()
        elif choice == '2':
            clear()
            sign_in()
        elif choice == '3':
            clear()
            check_balance()
        elif choice == '4':
            clear()
            deposit()
        elif choice == '5':
            clear()
            withdraw()
        elif choice == '6':
            clear()
            transfer()
        elif choice == '7':
            clear()
            payment()
        elif choice == '8':
            clear()
            loan()
        elif choice == '9':
            clear()
            profile()
        elif choice == '10':
            clear()
            payback()
        
        elif choice == '12':
            clear()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display()