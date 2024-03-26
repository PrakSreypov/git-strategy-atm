users = {
    "user1": {"password": "1234", "balance": 1000, 'Loan': 0},
    "user2": {"password": "5678", "balance": 2000, 'Loan': 0}
}
current_user = None


def sign_up():
    global users
    print("---- create an account ----")
    username = input("name: ")
    if username in users:
        print("Username already exists. Please choose another username.")
        return
    password = input("Set password: ")
    phone = input("Phone Number:")
    #balance = float(input("Enter initial balance: "))
    users[username] = {"password": password, "balance": 0, 'Loan': 0}
    current_user = username
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
            print(f"Welcome  {username}  ")
            break
                
        else:
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
                users[current_user]['balance'] -= amount
                users[recipient]['balance'] += amount
                print(f"Transferred ${amount} to {recipient} successfully.")
        else:
            print("Recipient not found.")

def withdraw():
    global users, current_user
    if current_user:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            print(f"Withdrew ${amount} successfully. New balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in first.")

# B Bonthong 
def check_balance():
    global users, current_user
    if current_user:
        print(f"Your balance is: {users[current_user]['balance']}")
    else:
        print("Please sign in first.")



def deposit():
    global users, current_user
    if current_user:
        amount = float(input("Enter amount to deposit: "))
        users[current_user]['balance'] += amount
        print(f"Deposited ${amount}. New balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in first.")




def payment():
    if current_user:
        recipient = input("Enter payment recipient: ")
        amount = float(input("Enter payment amount: "))
        if amount <= users[current_user]["balance"]:
            users[current_user]["balance"] -= amount
            print(f"Payment of ${amount} to {recipient} successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Please sign in to make a payment.")

def loan():
    if current_user:
        amount = float(input("Enter loan amount: "))
        users[current_user]["balance"] += amount
        print(f"Loan of ${amount} credited to your account. New balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in to apply for a loan.")

def profile():
    global users, current_user
    if current_user:
        print(f"Balance: ${users[current_user]['balance']}")
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
        print("10. Logout")
        print("11. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            deposit()
        elif choice == '5':
            withdraw()
        elif choice == '6':
            transfer()
        elif choice == '7':
            payment()
        elif choice == '8':
            loan()
        elif choice == '9':
            profile()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display()