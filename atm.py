from datetime import datetime
class User:
    def __init__(self, user_id, pin, balance):
        self.balance = balance
        self.user_id = user_id
        self.pin = pin
class Transaction:
    def __init__(self, amount, transaction_type, timestamp):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp
class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to hold user ID as key and User object as value
        self.transactions = []  # List to hold Transaction objects

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return True
        return False

    def deposit(self, user_id, amount):
    
        if amount <= 0:
            print("Invalid amount for deposit.")
            return

        # Add amount to user balance
        self.users[user_id].balance += amount

        # Add transaction to the list
        transaction = Transaction(amount, "Deposit", datetime.now())
        self.transactions.append(transaction)

        print("Deposit successful. Current balance:", self.users[user_id].balance)

    def withdraw(self, user_id, amount):
    
        if amount <= 0:
            print("Invalid amount for withdrawal.")
            return

        if amount > self.users[user_id].balance:
            print("Insufficient funds.")
            return

        # Deduct amount from user balance
        self.users[user_id].balance -= amount

        # Add transaction to the list
        transaction = Transaction(amount, "Withdrawal", datetime.now())
        self.transactions.append(transaction)

        print("Withdrawal successful. Current balance:", self.users[user_id].balance)

    def transfer(self, user_id, recipient_id, amount):
        if amount <= 0:
            print("Invalid amount for transfer.")
            return

        if user_id not in self.users or recipient_id not in self.users:
            print("Invalid user ID.")
            return

        if amount > self.users[user_id].balance:
            print("Insufficient funds for transfer.")
            return

        # Deduct amount from sender's balance
        self.users[user_id].balance -= amount
       
    def show_transaction_history(self, user_id):
        # Display transaction history for the user
        print("Transaction History for User:", user_id)
        for transaction in self.transactions:
            if transaction.transaction_type.startswith("Transfer to " + user_id) or transaction.transaction_type.startswith("Transfer from " + user_id):
                print("- Type:", transaction.transaction_type)
                print("  Amount:", transaction.amount)
                print("  Timestamp:", transaction.timestamp)
            elif transaction.transaction_type != "Transfer to " + user_id and transaction.transaction_type != "Transfer from " + user_id:
                print("- Type:", transaction.transaction_type)
                print("  Amount:", transaction.amount)
                print("  Timestamp:", transaction.timestamp)
def main():
    atm = ATM()

    # Sample user creation
    user1 = User("prithika", "1234",1000)
    user2 = User("Abhinaya","123",1000)
    atm.users[user1.user_id] = user1
    atm.users[user2.user_id] = user2

    # Main loop
    while True:
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        if atm.authenticate_user(user_id, pin):
            print("Authentication successful!")
            while True:
                print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Transaction History\n5. Quit")
                choice = input("Enter choice: ")

                if choice == "1":
                    amount = float(input("Enter deposit amount: "))
                    atm.deposit(user_id, amount)
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    atm.withdraw(user_id, amount)
                elif choice == "3":
                    recipient_id = input("Enter recipient ID: ")
                    amount = float(input("Enter transfer amount: "))
                    atm.transfer(user_id, recipient_id, amount)
                elif choice == "4":
                    atm.show_transaction_history(user_id)
                elif choice == "5":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice!")
        else:
            print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()
