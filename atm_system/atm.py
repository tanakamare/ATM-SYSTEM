"""
Simple ATM System
This program simulates a basic ATM with the following features:
- Check balance
- Deposit money
- Withdraw money
- Exit
"""

class ATM:
    def __init__(self, balance=0):
        """Initialize the ATM with a starting balance"""
        self.balance = balance
        self.transaction_history = []
    
    def check_balance(self):
        """Display the current balance"""
        return self.balance
    
    def deposit(self, amount):
        """Add money to the account"""
        if amount <= 0:
            return "Invalid amount. Please enter a positive number."
        
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return f"${amount} deposited successfully. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Remove money from the account if sufficient funds are available"""
        if amount <= 0:
            return "Invalid amount. Please enter a positive number."
        
        if amount > self.balance:
            return f"Insufficient funds. Your balance is ${self.balance}"
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return f"${amount} withdrawn successfully. New balance: ${self.balance}"
    
    def view_history(self):
        """View transaction history"""
        if not self.transaction_history:
            return "No transaction history available."
        
        history = "Transaction History:\n"
        for transaction in self.transaction_history:
            history += f"- {transaction}\n"
        history += f"Current Balance: ${self.balance}"
        
        return history

def main():
    # Create an ATM instance with initial balance of $1000
    atm = ATM(1000)
    
    while True:
        # Display menu
        print("\n===== Welcome to Simple ATM =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            balance = atm.check_balance()
            print(f"\nYour current balance is: ${balance}")
            
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: $"))
                result = atm.deposit(amount)
                print(f"\n{result}")
            except ValueError:
                print("\nPlease enter a valid number.")
            
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                result = atm.withdraw(amount)
                print(f"\n{result}")
            except ValueError:
                print("\nPlease enter a valid number.")
                
        elif choice == '4':
            history = atm.view_history()
            print(f"\n{history}")
            
        elif choice == '5':
            print("\nThank you for using Simple ATM. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()