

accounts={}
account_number=1001
balance={}
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

    with open("customers.txt","a")as customers_file:
        customers_file.write(coustomer_info)
        
    with open("user.txt","a")as user_file:
        user_file.write(user_info)

def create_account():
    global account_number
    name=input("Enter the account holder name:")
    if account_number in accounts:
        print("account not found")
        return
    try:
        balance=float(input("Enter initial balance:"))
        if balance<500:
            print("initial amount must be greater than 500 ")
        return
    except ValueError:  
        print("invalid number")
    return
    accounts[account_number]= {
        "name":name,
        "balance":balance
        }
    print('Account created successfully!')
    account_number +=1

def account_saving():
    global account_number
    with open("account.txt","a")as file:
        if account_number in accounts:
            file.write(f"{accounts['username']},{accounts['password']}\n")
        print("Account saving successfully!")




def deposit():
    account=input("Enter the account number:")
    if account not in accounts:
        print("account not found:")
        amount=float(input("Enter the deposit amount:"))
    if amount <= 0:
        print("deposit amount. Must be positive number.")
        return balance
    balance += amount
    print(f"deposit successfully!,{amount}.new balance:{balance}")

    return balance


def withdraw():
    account=input("Enter the account number:")
    if account not in accounts:
        print("account not found:")
        amount=float(input("Enter thr withdraw amount:"))
        if amount <= 0:
            print("invalid amount. Must be greater than 0.")
        return
    if account[account[balance]]<amount:
        print("insufficient funds.")
    else:
        print(f"withdraw successfully!,{amount}.currentbalance:{balance}")
    return balance


def check_balance():
    input("Enter the acount_number:")
    if account_number in accounts:
        print("your current balance is: {balance}")



def transaction_history(deposit,withdraw):
    input("Enter the account number:")
    if account_number in accounts:
        print("transaction_history:")

def main_menu():
    while True:
        print("Menu-Driven")
        print("1.Create account")
        print("2.Deposit Money")
        print("3.withdraw Money")
        print("4.Check Balance")
        print("5.Transaction")
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