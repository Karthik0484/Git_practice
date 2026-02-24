class BankAccount:
    bank_name = "ABC Bank"   
    total_accounts = 0

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance   
        BankAccount.total_accounts += 1
#
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Karthik", 5000)
acc1.deposit(1000)
acc1.withdraw(2000)
print(acc1.get_balance())


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"Employee: {self.name}"


class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.allowance


# # Polymorphism
employees = [
    Developer("Karthik", 50000, 10000),
    Manager("Rahul", 60000, 15000)
]

for emp in employees:
    print(emp.name, "Salary:", emp.calculate_salary())


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount(self):

    """
    Calculates the discount for the product.

    This method should be overridden by sub-classes to provide the
    discount calculation logic specific to their product type.

    Returns:
        float: The discount amount
    """
        raise NotImplementedError("Subclasses must implement this method")

    def final_price(self):
        return self.price - self.calculate_discount()


class Electronics(Product):
    def calculate_discount(self):
        return self.price * 0.10   


class Clothing(Product):
    def calculate_discount(self):
        return self.price * 0.20 

products = [
    Electronics("Laptop", 50000),
    Clothing("T-Shirt", 2000)
]

for p in products:
    print(f"{p.name} Final Price: {p.final_price()}")