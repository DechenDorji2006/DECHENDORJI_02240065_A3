import random
import tkinter as tk
from tkinter import messagebox
class InvalidUserInput(Exception): # This code is for to handle invalid user input
    pass

class InvalidTransferRequest(Exception): #this code for to handle invalid transfer request
    """Raised when a transfer cannot be completed."""
    pass

class Making_Bank_Account:  #this code is for to make a bank account
    """Base class for bank account.""" 
    def __init__(self, Acct_Id, PassCode, Account_Type, Money=0): #this code is for constructor of the class
        self.Acct_ID = Acct_Id
        self.PassCode = PassCode
        self.Account_Type = Account_Type
        self.Money_Balance = Money
        self.Phone_Recharge = 0  # New: for mobile top-up

    def deposit_money(self, money):    # =this code is for to deposit money into other account
        """This code funtion to deposit money in account,
          how it works is that the user will input the amount they want to deposit,
            if the money greater than 0 then it will be deposited into the account otherwise it will 
            return invalid fund amount"""
        if money > 0:
            self.Money_Balance += money
            return "Deposit is successful."
        return "Invalid fund amount."

    def witdraw(self, fund): #this code is used for withdrawing money from the account
        """Withdraw money code, it will check if the fund is greater
          than 0 and less than or equal to the account balance,"""
        if 0 < fund <= self.Money_Balance:
            self.Money_Balance -= fund
            return "Withdrawal successful."
        return "Shortage of MOney"

    def transfer(self, amount, reciver_acct):   #transfer function
        """Transfer money to other account code, it will 
        check if the amount is greater than 0 and less 
        than or equal to the account balance, them it will transfer the money to the other account"""
        if amount <= 0 or amount > self.Money_Balance:
            return "Invalid Transfer amount."
        self.Money_Balance -= amount
        reciver_acct.funds += amount
        return "Transfer completed."

    def phone_top_up(self, money):
        """Recharge mobile data from available bank balnce, if the money is greater than 0 and less than or equal to the account balance,
        then it will recharge the phone balance, otherwise it will return invalid top-up amount."""
        if 0 < money <= self.Money_Balance:
            self.Money_Balance -= money
            self.Phone_Recharge += money
            return f"Phone is recharged, Phone balance: {self.Phone_Recharge}"
        return "Invalid top-up amount."

"""Making the bank acoont classes for different account types. checking 
the account type is Personal or Business."""
class Personal_Bank_Account(Making_Bank_Account):
    def __init__(self, account_id, passcode, funds=0):
        super().__init__(account_id, passcode, "Personal_account", funds)

class Business_Bank_Account(Making_Bank_Account):
    def __init__(self, account_id, passcode, funds=0):
        super().__init__(account_id, passcode, "Business_account", funds)


class Banking_function:
    """code that manages the bank accounts."""
    def __init__(self):
        self.class_Accounts = {}

    def create_new_account(self, account_type):
        """code that function new account creation. how it works is that the user will input the account type 
        then it will display random account ID and passcode,"""
        Account_Id = str(random.randint(10000, 99999))  # it will give a random account ID
        Pass_code = str(random.randint(1000, 9999)) #it will provide a random passcode within given range
        if account_type == "Personal":
            account = Personal_Bank_Account(Account_Id, Pass_code)
        else:
            account = Business_Bank_Account(Account_Id, Pass_code)
        self.class_Accounts[Account_Id] = account
        return account

    def login_account(self, Account_id, Passcode):
        """Login to account but it will only work if the account exist"""
        account = self.class_Accounts.get(Account_id)
        if account and account.passcode == Passcode:
            return account
        print("wrong account ID or passcode")
        return None

    def delete_existing_account(self, Account_id):
        """Delete an existing account."""
        """This code will delete the account if it exists."""
        if Account_id in self.class_Accounts:
            self.class_Accounts.pop(Account_id)
            return True
        return False


def process_user_input(option, BANK):
    """Code is for main menu """
    if option == "1":
        acct_Type = input("Enter your account type (Personal/Business): ")
        if acct_Type not in ["Personal", "Business"]:
            print("Invalid")
            return True
        Account = BANK.create_new_account(acct_Type)
        print(f"New Account is Created! please rember the ID and Passcode ID: {Account.Acct_ID}, Passcode: {Account.PassCode}")

    elif option == "2":
        account_id = input("Type Account ID: ")
        password = input("Enter passcode: ")
        try:
            Account = BANK.login(account_id, password)
            while True:
                print("\n1. Check_Bank_Balance \n2. Deposit fund\n3. Withdraw fund\n4. Transfer fund\n5. Data Recharge\n6. Delete Account\n7. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print(f"Current Balance: {Account.funds}")
                elif choice == "2":
                    Your_Fund = float(input("How much you want to deposit: "))
                    print(Account.deposit(Your_Fund))
                elif choice == "3":
                    Your_Fund = float(input("How mauch do you want to withdraw: "))
                    print(Account.withdraw(Your_Fund))
                elif choice == "4":
                    recieve_id = input("Reciever account ID: ")
                    Your_Fund = float(input("Transfer fund: "))
                    if recieve_id not in BANK.accounts:
                        print("Reciver account does not exist.")
                    else:
                        print(Account.transfer(Your_Fund, BANK.accounts[recieve_id]))
                elif choice == "5":
                    Your_Fund = float(input("Recharge amount: "))
                    print(Account.phone_top_up(Your_Fund))
                elif choice == "6":
                    BANK.delete_account(Account.account_id)
                    print("Account deleted.")
                    break
                elif choice == "7":
                    break
                else:
                    print("Invalid menu choice.")
        except Exception as e:
            print(f"Error: {e}")

    elif option == "3":
        print("Goodbye!")
        return False
    else:
        print("Invalid main menu choice.")
    return True


class Banking_sytem_GUI:
    def __init__(self):
        self.Bankk = Banking_function()
        self.currenting_account = None

        self.Window = tk.Tk() # ts function is to create a new window
        self.Window.title("Banking System") # this function is to set the title of the window

        tk.Label(self.Window, text="Account id").pack() 
        """how it work is that it will create a label with the text "Account id" and pack it into the window."""
        self.id_input = tk.Entry(self.Window)
        self.id_input.pack()
        tk.Label(self.Window, text="Passcode").pack()
        self.pass_entry = tk.Entry(self.Window, show="*")
        self.pass_entry.pack()
        """this code is to create a label with the text "Passcode" and pack it into the window."""
        tk.Button(self.Window, text="Login", command=self.login).pack()
        tk.Button(self.Window, text="Create Personal account", command=self.create_personal).pack()
        tk.Button(self.Window, text="Create Business account", command=self.create_business).pack()
        tk.Label(self.Window, text="Amount").pack()
        self.amount_entry = tk.Entry(self.Window)
        self.amount_entry.pack()
        tk.Button(self.Window, text="Deposit", command=self.deposit).pack()
        tk.Button(self.Window, text="Withdraw", command=self.withdraw).pack()
        tk.Button(self.Window, text="Top-Up", command=self.topup).pack()
        tk.Button(self.Window, text="Transfer Money", command=self.transfer_window).pack()
        self.result_label = tk.Label(self.Window, text="")
        self.result_label.pack()

    def transfer_window(self):
        if not self.currenting_account:
            self.result_label.config(text="Please login first.")
            return
        transfer_win = tk.Toplevel(self.Window)
        transfer_win.title("Transfer Money")

        tk.Label(transfer_win, text="Receiver Account ID:").pack()
        receiver_entry = tk.Entry(transfer_win)
        receiver_entry.pack()
        tk.Label(transfer_win, text="Amount:").pack()
        amount_entry = tk.Entry(transfer_win)
        amount_entry.pack()

        def do_transfer():
            receiver_id = receiver_entry.get()
            try:
                amount = float(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                return
            receiver = self.Bankk.class_Accounts.get(receiver_id)
            if not receiver:
                messagebox.showerror("Error", "Receiver account not found.")
                return
            msg = self.currenting_account.transfer(amount, receiver)
            messagebox.showinfo("Transfer", msg)
            transfer_win.destroy()

        tk.Button(transfer_win, text="Transfer", command=do_transfer).pack(pady=5)
        tk.Button(transfer_win, text="Cancel", command=transfer_win.destroy).pack(pady=5)
        
    def login(self):
        """This code is for to login into the account, how it works is that the user will input the account ID and passcode,
        then it will check if the account exist and if the passcode is correct, then it will login into the account."""

        acc_id = self.id_input.get()
        pwd = self.pass_entry.get()
        acc = self.Bankk.class_Accounts.get(acc_id)
        if acc and acc.PassCode == pwd:
            self.currenting_account = acc
            self.result_label.config(text=f"Logged in. Balance: {acc.Money_Balance}")
        else:
            self.result_label.config(text="Login failed.")

    def create_personal(self):# This code is for to create a personal account
        acc = self.Bankk.create_new_account("Personal")
        self.result_label.config(text=f"ID: {acc.Acct_ID}, Pass: {acc.PassCode}")

    def create_business(self):# This code is for to create a business account
        acc = self.Bankk.create_new_account("Business")
        self.result_label.config(text=f"ID: {acc.Acct_ID}, Pass: {acc.PassCode}")

    def deposit(self):# This code is for to deposit money into the account
        if self.currenting_account:
            try:
                amt = float(self.amount_entry.get())
                msg = self.currenting_account.deposit_money(amt)
                self.result_label.config(text=msg)
            except Exception:
                self.result_label.config(text="Invalid amount.")

    def withdraw(self):# This code is for to withdraw money from the account
        if self.currenting_account:
            try:
                amt = float(self.amount_entry.get())
                msg = self.currenting_account.witdraw(amt)
                self.result_label.config(text=msg)
            except Exception:
                self.result_label.config(text="Invalid amount.")

    def topup(self):# This code is for to top-up the phone balance
        if self.currenting_account:
            try:
                amt = float(self.amount_entry.get())
                msg = self.currenting_account.phone_top_up(amt)
                self.result_label.config(text=msg)
            except Exception:
                self.result_label.config(text="Invalid amount.")

    """This code is for to clear the screen and display the dashboard screen.
    """
    def simple_transaction_screen(self, action_name, transaction_func):
        self.clear_screen()
        tk.Label(self.root, text=f"{action_name} Money").pack(pady=10)
        entry = tk.Entry(self.root)
        entry.pack()

        def do_transaction():
            try:
                amount = float(entry.get())
                result = transaction_func(amount)
                messagebox.showinfo(action_name, result)
                self.dashboard_screen()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")

        tk.Button(self.root, text=f"{action_name}", command=do_transaction).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack(pady=5)


    def run(self):
        self.Window.mainloop()

if __name__ == "__main__":
    gui = Banking_sytem_GUI()
    gui.run()
