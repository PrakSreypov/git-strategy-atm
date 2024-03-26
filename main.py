users = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "5678", "balance": 2000}
}
current_user = None

def loan():
    if current_user:
        amount = float(input("Enter loan amount: "))
        users[current_user]["balance"] += amount
        print(f"Loan of ${amount} credited to your account. New balance: ${users[current_user]['balance']}")
    else:
        print("Please sign in to apply for a loan.")