from Person import Person

value = 10
print("Hello")
print(value)

person_1 = Person("Kasun",19)
person_2 = Person("Supun",35)
person_3 = Person("Nimal",28)
person_4 = Person("Chathu",21)
person_5 = Person("Sanka", 25)
person_6 = Person("Sandun",23)

print(person_1.age)
print(person_2.name)
print(person_5.age)
print(person_6.name)





from customer import Customer
from employee import Employee
from shop import Shop
from product import Product

def main():
    # Create a shop
    shop = Shop("Tech Store")

    # Create and add customers
    customer1 = Customer("Alice", 30, "C001")
    customer2 = Customer("Bob", 24, "C002")
    shop.add_customer(customer1)
    shop.add_customer(customer2)


    # Create and add employees
    employee1 = Employee("Charlie", 28, "E001", "Manager")
    employee2 = Employee("Diana", 22, "E002", "Sales Assistant")
    shop.add_employee(employee1)
    shop.add_employee(employee2)

    # Create and add products
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 699.99, 15)
    shop.add_product(product1)
    shop.add_product(product2)

    # Print shop details
    print(shop)
