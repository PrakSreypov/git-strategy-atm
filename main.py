users = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "5678", "balance": 2000}
}
current_user = None
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
    else:
        print("Please sign in first.")