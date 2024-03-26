users = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "5678", "balance": 2000}
}
current_user = None
def withdraw():
    global users, current_user
    if current_user:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            print(f"Withdrew ${amount} successfully.")
    else:
        print("Please sign in first.")