import os
from datetime import datetime

accounts={}
account_number=int(1001)

def trans():
    with open("transaction.txt","a")as file:
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time}-{account_number}{amount}{balance}") 
def get_customer_info():
    customer_name =input("Enter the name:")
    customer_address =input("Enter the address:")
    email_id =input("Enter the email id:")
    user_name=input("Enter the username:")
    password =input("Enter the password:")
    create_customer(customer_name,customer_address,email_id,user_name,password)

    return(customer_name,customer_address,email_id,user_name,password)


def create_customer(customer_name,customer_address,email_id,user_name,password):
    coustomer_info=f"{customer_name},{customer_address},{email_id}/n"
    user_info=f"{user_name},{password}/n"

    with open("customers.txt","w")as customers_file:
        customers_file.write(coustomer_info)
        
    with open("user.txt","w")as user_file:
        user_file.write(user_info)

# def account_saving():
#     global account_number
#     with open("account.txt","w")as file:
#         file.write(f"{account_number},{data["username"]},{data["password"]},{data["email_id"]},{data["balance"]}")

def create_account():
    global account_number
    global accounts
    name=input("Enter the account holder name:")
    
    try:
        initial_balance=float(input("Enter initial balance:"))
        if initial_balance<500:
            print("initial amount must be greater than 500 ")
            return
    except ValueError:  
        print("invalid number")
        return
    accounts[account_number]= {
        "name":name,
        "balance": initial_balance,
        "transaction" : f"initiated balance is {initial_balance} "
        }
    

    # account_saving()
    print('Account created successfully!')
    print(f"your acc number is {account_number}")
    account_number +=1



def deposit():
    global amount 
    try:
        account_number=int(input("Enter the account number:"))
        if account_number not in accounts:
            print("account not found:")
        
        elif account_number in accounts :
            amount=float(input("Enter the deposit amount:"))
            if amount < 0 :
                print("deposit amount. Must be positive number.")
            else:
                accounts[account_number]["balance"] += amount
                accounts[account_number]["transaction"].append[f"deposited : {amount}"]   

    #     # account_saving()
    #     # trans()
                print(f"deposit successfully!,{amount}.new balance:{accounts[account_number]["balance"]} ")
            return amount
        
    except ValueError:
        print("invalid input")

    # accounts[account_number]["transaction"].append[f"deposited : {amount}"]   



def withdraw():
    global amount 
    try :
        account_number=int(input("Enter the account number:"))
        if account_number not in accounts:
            print("account not found:")
        
        elif account_number in accounts :
            amount=float(input("Enter the withdrawal amount:"))
            if amount < 0 :
                print("withdraw amount must be positive")
            elif amount > accounts[account_number]['balance'] :
                print("insufficient balance")
            else:
                accounts[account_number]["balance"] -= amount
                accounts[account_number]["transaction"].append[f"withdrew : {amount}"]

        # account_saving()
        # trans()
                print(f"withdrew successfully!,{amount}.new balance:{accounts[account_number]["balance"]} ")
            return amount
        
    except ValueError:
        print("invalid input")

    # accounts[account_number]["transaction"].append[f"withdrew : {amount}"]

    
def check_balance():
    account_number=int(input("Enter the acount_number:"))
    if account_number in accounts:
        print(f"your current balance is: {accounts[account_number]['balance']}")
    else:
        print("account not found!")


def transaction_history():
    #    account= input("Enter the account number:")
    #    with open("transaction.txt","a")as file:
    #        if not os.path.exists("transaction"):
    #            print("Not any transaction")
    #            return
    #        else:
    #             with open("transaction.txt","r")as file:
    #                 for line in file:
    #                     if line.strip().split("-")[1]==str(account):
    #                         print(line.strip)
                            
    account_number = int(input("Enter the account number:"))

    if account_number in accounts:
        print(f"transaction histiory{account_number}:")
        for transaction in accounts[account_number]["transaction"] :
            print("-", transaction )

        

def main_menu():
    while True:
        print("Menu-Driven")
        print("1.Create account")
        print("2.Deposit Money")
        print("3.withdraw Money")
        print("4.Check Balance")
        print("5.Transaction History")
        print("6.Exit")

        choice = input("Enter your choice (1-6):")
  
        if choice == "1":
            create_account()
        elif choice =="2":
            deposit()
        elif choice =="3":
            withdraw()
        elif choice =="4":
            check_balance()
        elif choice =="5":
            transaction_history()
        elif choice =="6":
            print("Thank you so much for reaching us!")
            break
        else:
            print("exit")

main_menu()
