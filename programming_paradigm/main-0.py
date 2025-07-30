# main-0.py
import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if account.deposit(amount):
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Deposit failed. Amount must be positive.")
        
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Withdrawal failed. Check your balance or amount.")
        
        elif choice == '3':
            account.display_balance()
        
        elif choice == '4':
            print("Exiting the program.")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
