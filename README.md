class BankAccount:
    def __init__(self):
        self.money = self.moneyload()

    def moneyload(self):
        try:
            with open("moneylist.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    return 0
                return int(lines[-1].split(" | ")[-1])
        except FileNotFoundError:
            return 0
        
    def save(self, action , amount):
        with open("moneylist.txt", "a", encoding="utf-8") as f:
            f.write(f"{action} | {amount} | {self.money}\n")
    
    def addmn(self, amount):
        self.money += amount
    
    def minmn(self, amount):
        self.money -= amount

class Deposit:
    def __init__(self, account):
        self.account = account
    
    def deposit(self):
        try:
            amount = int(input("How much would you like to deposit? "))
            if amount <= 0:
                print("Invalid Input.")
                return
            self.account.addmn(amount)
            self.account.save("Deposit", amount)
            print(f"{amount} won(s) successfully deposited.")
        except ValueError:
            print("This amount cannot be deposited.")

class Withdraw:
    def __init__(self, account):
        self.account = account

    def withdraw(self):
        try:
            amount = int(input("How much would you like to withdraw? "))
            if amount <= 0:
                print("Invalid Input.")
                return
            if self.account.money < amount:
                print("Not enough money.")
                return
            self.account.minmn(amount)
            self.account.save("Withdraw", amount)
            print(f"{amount} won(s) succesfully withdrawn.")
        except ValueError:
            print("This amount can't be withdrawn.")

account = BankAccount()
deposit = Deposit(account)
withdraw = Withdraw(account)

print(f"Loaded money: {account.money} Won(s).")

while True:
    menu = input("Deposit / Withdraw / Money / End: ").lower()
    if menu == "deposit":
        deposit.deposit()

    elif menu == "withdraw":
        withdraw.withdraw()
    
    elif menu == "money":
        print(f"Current Money: {account.money} Won(s).")
    
    elif menu == "end":
        print("Program Ended.")
        break

    else:
        print("Invalid Input.")
        continue
