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