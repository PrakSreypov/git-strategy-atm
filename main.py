users = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "5678", "balance": 2000}
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
    #balance = float(input("Enter initial balance: "))
    users[username] = {"password": password, "balance": 0}
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
<<<<<<< HEAD


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
            print(f"Withdrew ${amount} successfully.")
    else:
        print("Please sign in first.")

# B Bonthong 
def check_balance():
    global users, current_user
    if current_user:
        print(f"Your balance is: {users[current_user]['balance']}")
    else:
        print("Please sign in first.")

=======
def profile():
    global users, current_user
    if current_user:
        print(f"Balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in first.")
>>>>>>> 2745951 (add a profile)
