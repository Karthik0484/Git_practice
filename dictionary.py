'''Q1. Inventory Update

You are given:
inventory = {"apple": 10, "banana": 5}
sales = {"apple": 3, "banana": 2}

Update inventory after sales.'''

inventory = {"apple": 10, "banana": 5}
sales = {"apple": 3, "banana": 2}

for items,qty in sales.items():
    if items in inventory:
        inventory[items] -= qty

print(inventory)
print()



'''Q2. Login Attempt Tracker

Given login logs:
logs = ["Alice", "Bob", "Alice", "Alice", "Bob"]
Create a dictionary showing number of login attempts per user.'''

logs = ["Alice", "Bob", "Alice", "Alice", "Bob"]
login_count={}

for name in logs:
    if name in login_count:
        login_count[name] += 1
    else:
        login_count[name] = 1
print(login_count)