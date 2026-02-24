'''Q1. Modular Billing System

Create functions:
calculate_tax(price)
apply_discount(price)
final_bill(price)'''

def calculate_tax(price):
    tax = price * 0.18
    return tax

def apply_discount(price):
    discount = price * 0.1
    return discount

def final_bill(price):
    tax = calculate_tax(price)
    discount_new = apply_discount(price)
    final = price + tax - discount_new
    return final

Bill = final_bill(100)
print("Final Bill: ", Bill)

# Q2. ATM System Using Functions

balance = 0

def deposit(amount):
    global balance
    print(" Amount you deposit: ", amount)
    balance += amount
    return balance

def withdraw(amt):
    global balance
    if amt <= balance:
        print("Amount Withdrawn: ",amt)
        balance -= amt
    else:
        print("Insufficient Balance")
    return balance

def check_balance():
    return balance

deposit(1000)
withdraw(500)
final_balance = check_balance()
print("Balance : ", final_balance)