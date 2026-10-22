from pract_07 import employee

from dataclasses import dataclass




class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def display(self):
        print(f"{self.name} : {self.salary}")

employee1 = Employee("Amit", 50000)

employee1.display()


#inheriatance

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def code(self):
        print(f"{self.name} writes {self.language}")


developer = Developer("Saurabh", 60000, "Python")
developer.display()
developer.code()



#Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(5000)

print(account.get_balance())

#DataClasses

@dataclass
class Product:
    id: int
    name:str
    price:float

product = Product(1 , "keyboard",1200.0)

print(product)
print(product.name)

