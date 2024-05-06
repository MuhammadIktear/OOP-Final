import random
from datetime import datetime

#bank
class bank:
    def __init__(self,name) -> None:
        self.initial_bank_balance=1000000

#user
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.accounts = {}
        self.transaction_history = []
        self.max_loan_times = 2

    def create_account(self, password, account_type):
        account_number = random.randint(1000, 99999)
        self.accounts[account_number] = {'name': self.name, 'email': self.email, 'address': self.address,
                                         'account_type': account_type, 'password': password, 'balance': 0}
        print(f"{account_type} account created successfully!")
        print("Your account number is:", account_number)

    def login(self, account_number, password):
        account_number = int(account_number)
        account = self.accounts.get(account_number)
        if account and account['password'] == password:
            print("Login successful!")
            return True
        else:
            print("Account number or password is incorrect.")
            return False

    def withdraw_amount(self, account_number, amount):
        account_number=int(account_number)
        account = self.accounts.get(account_number)
        if not account:
            print("Account does not exist.")
            return
        if(Bankrupt_bank.initial_bank_balance<=amount):
            if account['balance'] >= amount:
                account['balance'] -= amount
                Bankrupt_bank.initial_bank_balance-=amount 
                self.transaction_history.append({'account_number': account_number, 'transaction_type': 'Withdraw',
                                                'amount': amount, 'date_time': datetime.now()})
                print(f"{amount} has been withdrawn.")
            else:
                print("Withdrawal amount exceeds your balance.")
        else:
            print("Bank is Bankrupt")

    def deposit(self, account_number, amount):
        account_number=int(account_number)
        account = self.accounts.get(account_number)
        if not account:
            print("Account does not exist.")
            return
        Bankrupt_bank.initial_bank_balance+=amount   
        account['balance'] += amount
        self.transaction_history.append({'account_number': account_number, 'transaction_type': 'Deposit',
                                         'amount': amount, 'date_time': datetime.now()})
        print(f"{amount} has been deposited.")

    def transfer_amount(self, sender_account_number, recipient_account_number, amount):
        sender_account = self.accounts.get(sender_account_number)
        recipient_account = self.accounts.get(recipient_account_number)

        if not sender_account or not recipient_account:
            print("Sender or recipient account does not exist.")
            return

        if sender_account['balance'] >= amount:
            sender_account['balance'] -= amount
            recipient_account['balance'] += amount
            self.transaction_history.append({'sender_account_number': sender_account_number,
                                             'recipient_account_number': recipient_account_number,
                                             'transaction_type': 'Transfer', 'amount': amount,
                                             'date_time': datetime.now()})
            print(f"{amount} transferred successfully to account number {recipient_account_number}.")
        else:
            print("Insufficient balance for transfer.")

    def apply_for_loan(self, account_number, amount,loan_system_enabled):
        account_number=int(account_number)
        if amount<=admin.loan_limit:
            if self.max_loan_times > 0 and loan_system_enabled:
                self.max_loan_times -= 1
                Bankrupt_bank.initial_bank_balance-=amount
                self.accounts[account_number]['balance'] += amount
                self.transaction_history.append({'transaction_type': 'Loan', 'amount': amount,
                                                'date_time': datetime.now()})
                print(f"{amount} loan successfully added to your account.")
            else:
                print("You have already reached the maximum number of loans or the loan system is disabled.")
        else:
            print(f"Maximum loan limit {admin.loan_limit} taka")


    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            transaction_type = transaction.get('transaction_type')
            amount = transaction.get('amount')
            date_time = transaction.get('date_time')
            print(f"Transaction Type: {transaction_type}, Amount: {amount}, Date-Time: {date_time.strftime('%Y-%m-%d %H:%M:%S') if isinstance(date_time, datetime) else 'N/A'}")

#admin
class Admin:
    def __init__(self):
        self.adminDetails = []
        self.loan_system_enabled = True
        self.loan_limit=10000
    def create_account(self, name, email, address, password):
        ID_number = random.randint(100, 999)
        self.adminDetails.append({'name': name, 'email': email, 'address': address, 'ID_number': ID_number,
                                  'password': password})
        print("Account created successfully!")
        print("Your ID number is:", ID_number)

    def login(self, id_number, password):
        for account in self.adminDetails:
            if account['ID_number'] == id_number and account['password'] == password:
                return True
        print("ID number or password is incorrect.")
        return False

    def delete_user(self, user_instance, account_number):
        account_number=int(account_number)
        if account_number in user_instance.accounts:
            del user_instance.accounts[account_number]
            print("Delete successful!")
        else:
            print("Account not found")

    def view_user_accounts(self, user_instance):
        if user_instance:
            print("User Accounts:")
            for account_number, account in user_instance.accounts.items():
                print(f"Account Number: {account_number}, Name: {account['name']}, Email: {account['email']}, Address: {account['address']}, Balance: {account['balance']}")
        else:
            print("No user account found.")

    def update_loan_system(self,loan_system_enabled):
        c=input("1. Enable\n2. disable\n")
        if c=='1':
            admin.loan_system_enabled=True
            print("Loan enable now")
        elif c=='2':
            admin.loan_system_enabled=False
            print("Loan disable now")
        else:
            print("Invalid input")

    def view_initial_bank_balance(self, user_instance):
        if user_instance:
            total_balance = sum(account['balance'] for account in user_instance.accounts.values())
            print(f"Total bank balance: {total_balance}")
        else:
            print("No user account found.")

    def view_total_loan(self, user_instance):
        if user_instance:
            total_loan = sum(transaction['amount'] for transaction in user_instance.transaction_history if transaction.get('transaction_type') == 'Loan')
            print(f"Total loan provided by the bank: {total_loan}")
        else:
            print("No user account found.")

#main
Bankrupt_bank=bank('Bankrupt Bank')
admin = Admin()
print("***Welcome to Bankrupt Bank***")

user_instances = []
admin_instance = Admin()

while True:
    choice = input("1. Create new account\n2. Login\n3. Exit\n")

    if choice == '1':
        account_type = input("1. Create new account as user\n2. Create new account as Admin\n")
        if account_type == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter a new password: ")
            user_instance = User(name, email, address)
            user_instances.append(user_instance)
            account_type = input("What type of account you want to create?\n1. Savings\n2. Current\n")
            if account_type == '1':
                user_instance.create_account(password, 'Savings')
            elif account_type == '2':
                user_instance.create_account(password, 'Current')
            else:
                print("Invalid Input")
        elif account_type == '2':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter a new password: ")
            admin_instance.create_account(name, email, address, password)
        else:
            print("Invalid Input")

    elif choice == '2':
        account_type = input("1. Login as user\n2. Login as Admin\n")
        if account_type=='1':
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            account_number = int(account_number)
            for user_instance in user_instances:
                try:
                    if user_instance.login(account_number, password):
                        while True:
                            operation = input("1. Deposit\n2. Withdraw\n3. Transfer\n4. Loan\n5. Transaction History\n6. Exit\n")
                            if operation == '1':
                                try:
                                    amount = float(input("Enter amount to deposit: "))
                                    user_instance.deposit(account_number, amount)
                                except ValueError:
                                    print("Invalid input. Please enter a valid amount.")
                            elif operation == '2':
                                try:
                                    amount = float(input("Enter amount to withdraw: "))
                                    user_instance.withdraw_amount(account_number, amount)
                                except ValueError:
                                    print("Invalid input. Please enter a valid amount.")
                            elif operation == '3':
                                recipient_account = input("Enter recipient account number: ")
                                try:
                                    amount = float(input("Enter amount to transfer: "))
                                    user_instance.transfer_amount(account_number, recipient_account, amount)
                                except ValueError:
                                    print("Invalid input. Please enter a valid amount.")
                            elif operation == '4':
                                try:
                                    amount = float(input("Enter loan amount: "))
                                    user_instance.apply_for_loan(account_number, amount,admin.loan_system_enabled)
                                except ValueError:
                                    print("Invalid input. Please enter a valid amount.")
                            elif operation == '5':
                                user_instance.show_transaction_history()
                            elif operation == '6':
                                print("Exiting user operations.")
                                break
                            else:
                                print("Invalid Input")
                except:
                    print("Account not found")                
        elif account_type=='2':
            id_number = input("Enter your Id number: ")
            password = input("Enter your password: ")
            id_number = int(id_number)
            if admin_instance.login(id_number, password):
                while True:
                    operation = input("1. View User Details\n2. Delete User Account\n3. View Bank Balance\n4. View Total Loan\n5. Loan System update(enable/disable)\n6 Exit\n")
                    if operation == '1':
                        admin_instance.view_user_accounts(user_instance)
                    elif operation == '2':
                        account_number = input("Enter account number to delete: ")
                        admin_instance.delete_user(user_instance, account_number)   
                    elif operation == '3':
                        print(f"Total bank balance: {Bankrupt_bank.initial_bank_balance}")
                    elif operation == '4':
                        try:
                            admin_instance.view_total_loan(user_instance)
                        except ValueError:
                            print("Loan amount zero")
                    elif operation == '5':
                            admin_instance.update_loan_system(admin.loan_system_enabled)
                    elif operation == '6':
                        print("Exiting admin operations.")
                        break
                    else:
                        print("Invalid Input")
        else:
            print("No user or admin account created yet.")

    elif choice == '3':
        print("Thank you for using Bankrupt Bank!")
        break

    else:
        print("Invalid Input")
