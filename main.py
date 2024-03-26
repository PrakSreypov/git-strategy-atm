users = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "5678", "balance": 2000}
}
current_user = None
def deposit():
    global users, current_user
    if current_user:
        amount = float(input("Enter amount to deposit: "))
        users[current_user]['balance'] += amount
        print(f"Deposited successfully. New balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in first.")