import random
import sys


class ATM():
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("\n ----------ACCOUNT DETAIL ----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: GH¢{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"An Amount of GH¢{amount} Has Been credited into your Account Successful!")
        print("Your Current Balance is: GH¢", self.balance)
        print("Thank for Banking With Us, All of us At Access Bank! ")
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Fund!")
            print(f"Your Balance is GH¢. {self.balance} only.")
            print("Try With Lesser Amount Than Balance.")
            print()
        else:
            self.balance = self.balance - amount
            print(f"An Amount of GH¢{amount} Has Been debited from your Account Successful!")
            print("Your Current Account Balance is: GH¢", self.balance)
            print()

    def check_balance(self):
        print("Available Balance : GH¢", self.balance)
        print()

    def transaction(self):
        print(""" TRANSACTION
        *******************************
        Menu:
        1. Account Details
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        *********************************
        """)
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5: "))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = float(input("How Much did you want to deposit (GH¢. ): "))
                    atm.deposit(amount)
                elif option == 4:
                    amount = float(input("How much did you want to Withdraw (GH¢. ): "))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
   Printing Receipt...................................
*************************************************************
    Transaction is now completed.
    Transaction number: {random.randint(10000, 1000000)}
    Account Holder: {self.name.upper()}
    Account Number: {self.account_number}
    Available Balance: GH¢. {self.balance}
    
    
    Thank for choosing us as your Bank
 *******************************************
 """)
                    sys.exit()


print("*******************WELCOME TO ACCESS BANK*********************")
print("----------------------------------------------------------------------------------\n")
print("---------ACCOUNT CREATION---------------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulation! Account Created Successfully ..........\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction (Yes/NO):")
    if trans == "Yes":
        atm.transaction()
    elif trans == "No":
        print("""----------------------------
        | Thanks for choosing us as your Bank |
        | Visit us Again!  At Access Bank     |              |
        --------------------------------------
        """)
        break
    else:
        print("Wrong Command! Enter Yes/NO \n")
