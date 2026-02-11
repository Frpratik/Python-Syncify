#==================================================================================
# COMPLETE OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON - BEGINNER FRIENDLY
#==================================================================================
"""
NOTES:
- OOP is a programming paradigm based on objects
- Objects contain data (attributes) and behavior (methods)
- Class is a blueprint for creating objects
- Helps organize code and model real-world entities
"""

#==================================================================================
# CLASSES AND OBJECTS
#==================================================================================
"""
NOTES:
- Class: Blueprint or template for objects
- Object: Instance of a class
- Example: 'Car' is a class, 'my_car' is an object
"""

print("--- CLASSES AND OBJECTS ---")

class Dog:
    pass

dog1 = Dog()
dog2 = Dog()

print("Created two Dog objects:")
print(f"dog1: {dog1}")
print(f"dog2: {dog2}")
print()

#==================================================================================
# ATTRIBUTES
#==================================================================================
"""
NOTES:
- Attributes are variables inside a class
- Store data about the object
"""

print("--- ATTRIBUTES ---")

class Person:
    pass

person1 = Person()
person1.name = "Alice"
person1.age = 25

print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print()

#==================================================================================
# __init__ METHOD (CONSTRUCTOR)
#==================================================================================
"""
NOTES:
- __init__ is called automatically when object is created
- Used to initialize object attributes
- 'self' refers to the object being created
"""

print("--- __init__ METHOD ---")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(f"Student 1: {student1.name}, Age: {student1.age}")
print(f"Student 2: {student2.name}, Age: {student2.age}")
print()

#==================================================================================
# METHODS
#==================================================================================
"""
NOTES:
- Methods are functions inside a class
- Define behavior of objects
- Always have 'self' as first parameter
"""

print("--- METHODS ---")

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

calc = Calculator(10, 5)
print(f"Addition: {calc.add()}")
print(f"Subtraction: {calc.subtract()}")
print()

#==================================================================================
# INSTANCE VARIABLES VS CLASS VARIABLES
#==================================================================================
"""
NOTES:
- Instance variables: Unique to each object (use self)
- Class variables: Shared by all objects
"""

print("--- INSTANCE VS CLASS VARIABLES ---")

class Employee:
    company = "TechCorp"  # Class variable (shared)
    
    def __init__(self, name, salary):
        self.name = name      # Instance variable (unique)
        self.salary = salary  # Instance variable (unique)

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"Employee 1: {emp1.name}, Company: {emp1.company}")
print(f"Employee 2: {emp2.name}, Company: {emp2.company}")
print()

#==================================================================================
# __str__ METHOD
#==================================================================================
"""
NOTES:
- __str__ defines how object is printed
- Returns a string representation
"""

print("--- __str__ METHOD ---")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

book1 = Book("Python Programming", "John Doe")
print(book1)
print()

#==================================================================================
# ENCAPSULATION (PRIVATE ATTRIBUTES)
#==================================================================================
"""
NOTES:
- Use double underscore (__) for private attributes
- Private attributes cannot be accessed directly
- Use methods to access/modify private data
"""

print("--- ENCAPSULATION ---")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(f"Owner: {account.owner}")
print(f"Balance: ${account.get_balance()}")
account.deposit(500)
print(f"After deposit: ${account.get_balance()}")
print()

#==================================================================================
# GETTERS AND SETTERS
#==================================================================================
"""
NOTES:
- Getter: Method to get private attribute
- Setter: Method to set private attribute with validation
"""

print("--- GETTERS AND SETTERS ---")

class Person2:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")
    
    def get_age(self):
        return self.__age

person = Person2("Alice", 25)
print(f"Name: {person.get_name()}")
person.set_age(26)
print(f"Age: {person.get_age()}")
print()

#==================================================================================
# @property DECORATOR
#==================================================================================
"""
NOTES:
- @property makes methods accessible like attributes
- Cleaner syntax than get/set methods
"""

print("--- @property DECORATOR ---")

class Employee2:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value

emp = Employee2("Alice", 5000)
print(f"Name: {emp.name}")
print(f"Salary: ${emp.salary}")
emp.salary = 5500
print(f"New salary: ${emp.salary}")
print()

#==================================================================================
# INHERITANCE - SINGLE INHERITANCE
#==================================================================================
"""
NOTES:
- Single Inheritance: One child class inherits from one parent class
- Child inherits all attributes and methods from parent
- Use super() to call parent class methods
"""

print("--- SINGLE INHERITANCE ---")

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return "walk walk"

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self): 
        return "Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.walk()}")
print(f"Sound: {dog.speak()}")
print()

#==================================================================================
# INHERITANCE - MULTIPLE INHERITANCE
#==================================================================================
"""
NOTES:
- Multiple Inheritance: Child class inherits from multiple parent classes
- Child gets features from all parent classes
"""

print("--- MULTIPLE INHERITANCE ---")

class Father:
    def __init__(self):
        self.father_name = "John"
    
    def gardening(self):
        return "I love gardening"

class Mother:
    def __init__(self):
        self.mother_name = "Jane"
    
    def cooking(self):
        return "I love cooking"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Tom"
    
    def info(self):
        return f"I am {self.child_name}"

child = Child()
print(f"Father: {child.father_name}")
print(f"Mother: {child.mother_name}")
print(f"Child: {child.child_name}")
print(child.gardening())
print(child.cooking())
print()

#==================================================================================
# INHERITANCE - MULTILEVEL INHERITANCE
#==================================================================================
"""
NOTES:
- Multilevel Inheritance: Child class inherits from parent, which inherits from grandparent
- Creates a chain of inheritance
"""

print("--- MULTILEVEL INHERITANCE ---")

class Grandparent:
    def __init__(self):
        self.grandparent_name = "William"
    
    def wisdom(self):
        return "Experience is the best teacher"

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self.parent_name = "John"
    
    def advice(self):
        return "Work hard"

class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.child_name = "Tom"
    
    def dream(self):
        return "I want to be successful"

child2 = Child2()
print(f"Grandparent: {child2.grandparent_name}")
print(f"Parent: {child2.parent_name}")
print(f"Child: {child2.child_name}")
print(child2.wisdom())
print(child2.advice())
print(child2.dream())
print()

#==================================================================================
# INHERITANCE - HIERARCHICAL INHERITANCE
#==================================================================================
"""
NOTES:
- Hierarchical Inheritance: Multiple child classes inherit from same parent
- Common features in parent, specific features in children
"""

print("--- HIERARCHICAL INHERITANCE ---")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
    
    def info(self):
        return f"Car with {self.doors} doors"

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type
    
    def info(self):
        return f"{self.type} bike"

car = Car("Toyota", 4)
bike = Bike("Yamaha", "Sports")

print(car.start())
print(car.info())
print(bike.start())
print(bike.info())
print()

#==================================================================================
# INHERITANCE - HYBRID INHERITANCE
#==================================================================================
"""
NOTES:
- Hybrid Inheritance: Combination of various inheritance types
- Mix of hierarchical and multiple inheritance
"""

print("--- HYBRID INHERITANCE ---")

class University:
    def __init__(self):
        self.university_name = "Tech University"

class Department(University):
    def __init__(self):
        super().__init__()
        self.dept_name = "Computer Science"

class Professor:
    def __init__(self):
        self.professor_name = "Dr. Smith"

class Student3(Department, Professor):
    def __init__(self):
        Department.__init__(self)
        Professor.__init__(self)
        self.student_name = "Alice"

student3 = Student3()
print(f"University: {student3.university_name}")
print(f"Department: {student3.dept_name}")
print(f"Professor: {student3.professor_name}")
print(f"Student: {student3.student_name}")
print()

#==================================================================================
# METHOD OVERRIDING
#==================================================================================
"""
NOTES:
- Child class can override (change) parent class methods
- Provides specific implementation for child class
"""

print("--- METHOD OVERRIDING ---")

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area()}")
print()

#==================================================================================
# POLYMORPHISM
#==================================================================================
"""
NOTES:
- Polymorphism: Same method name, different behavior
- Different classes can have methods with same name
"""

print("--- POLYMORPHISM ---")

class Dog2:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

def make_sound(animal):
    print(animal.speak())

dog2 = Dog2()
cat = Cat()
bird = Bird()

make_sound(dog2)
make_sound(cat)
make_sound(bird)
print()

#==================================================================================
# ABSTRACTION
#==================================================================================
"""
NOTES:
- Abstraction hides complex details
- Abstract class cannot be instantiated
- Child classes must implement abstract methods
"""

print("--- ABSTRACTION ---")

from abc import ABC, abstractmethod

class Shape2(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape2):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

square = Square(5)
print(f"Square area: {square.area()}")
print()

# #==================================================================================
# # COMPOSITION
# #==================================================================================
# """
# NOTES:
# - Composition: Object contains other objects
# - "Has-a" relationship
# - Example: Car has Engine
# """

# print("--- COMPOSITION ---")

# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
    
#     def start(self):
#         return "Engine started"

# class Car2:
#     def __init__(self, brand, horsepower):
#         self.brand = brand
#         self.engine = Engine(horsepower)
    
#     def start(self):
#         return f"{self.brand}: {self.engine.start()}"

# car2 = Car2("Toyota", 200)
# print(car2.start())
# print(f"Horsepower: {car2.engine.horsepower}")
# print()

# #==================================================================================
# # AGGREGATION
# #==================================================================================
# """
# NOTES:
# - Aggregation: Weaker "has-a" relationship
# - Objects can exist independently
# - Example: Department has Employees
# """

# print("--- AGGREGATION ---")

# class Employee3:
#     def __init__(self, name):
#         self.name = name

# class Department:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []
    
#     def add_employee(self, employee):
#         self.employees.append(employee)

# emp1 = Employee3("Alice")
# emp2 = Employee3("Bob")

# dept = Department("IT")
# dept.add_employee(emp1)
# dept.add_employee(emp2)

# print(f"Department: {dept.name}")
# print(f"Employees: {emp1.name}, {emp2.name}")
# print()

#==================================================================================
# STATIC METHODS
#==================================================================================
"""
NOTES:
- Static methods don't use self
- Called using class name
- Utility functions related to class
"""

print("--- STATIC METHODS ---")

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(f"5 + 3 = {Math.add(5, 3)}")
print(f"5 × 3 = {Math.multiply(5, 3)}")
print()

# #==================================================================================
# # CLASS METHODS
# #==================================================================================
# """
# NOTES:
# - Class methods receive class as first argument (cls)
# - Can modify class state
# - Often used as alternative constructors
# """

# print("--- CLASS METHODS ---")

# class Person3:
#     count = 0
    
#     def __init__(self, name):
#         self.name = name
#         Person3.count += 1
    
#     @classmethod
#     def get_count(cls):
#         return f"Total persons: {cls.count}"

# person1 = Person3("Alice")
# person2 = Person3("Bob")
# print(Person3.get_count())
# print()

# #==================================================================================
# # OPERATOR OVERLOADING
# #==================================================================================
# """
# NOTES:
# - Customize how operators work with objects
# - Use special methods (__add__, __sub__, etc.)
# """

# print("--- OPERATOR OVERLOADING ---")

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2

# print(f"p1 = {p1}")
# print(f"p2 = {p2}")
# print(f"p1 + p2 = {p3}")
# print()

# #==================================================================================
# # isinstance() AND issubclass()
# #==================================================================================
# """
# NOTES:
# - isinstance() checks if object is instance of class
# - issubclass() checks if class is subclass of another
# """

# print("--- isinstance() AND issubclass() ---")

# class Animal2:
#     pass

# class Dog3(Animal2):
#     pass

# dog3 = Dog3()

# print(f"dog3 is instance of Dog3: {isinstance(dog3, Dog3)}")
# print(f"dog3 is instance of Animal2: {isinstance(dog3, Animal2)}")
# print(f"Dog3 is subclass of Animal2: {issubclass(Dog3, Animal2)}")
# print()

# #==================================================================================
# # METHOD RESOLUTION ORDER (MRO)
# #==================================================================================
# """
# NOTES:
# - MRO determines order in which methods are searched
# - Important in multiple inheritance
# """

# print("--- METHOD RESOLUTION ORDER ---")

# class A:
#     def method(self):
#         return "A"

# class B(A):
#     def method(self):
#         return "B"

# class C(A):
#     def method(self):
#         return "C"

# class D(B, C):
#     pass

# d = D()
# print(f"Calling d.method(): {d.method()}")
# print("MRO for class D:")
# for i, cls in enumerate(D.mro(), 1):
#     print(f"{i}. {cls.__name__}")
# print()

#==================================================================================
# REAL-LIFE EXAMPLE 1: LIBRARY SYSTEM
#==================================================================================

print("--- EXAMPLE 1: LIBRARY SYSTEM ---")

class Book2:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' borrowed"
        return "Already borrowed"
    
    def return_book(self):
        self.is_borrowed = False
        return f"'{self.title}' returned"

book = Book2("Python Programming", "John Doe")
print(book.borrow())
print(book.return_book())
print()

#==================================================================================
# REAL-LIFE EXAMPLE 2: BANK ACCOUNT
#==================================================================================

print("--- EXAMPLE 2: BANK ACCOUNT ---")

class Account2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited ${amount}"
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}"
        return "Insufficient funds"
    
    def get_balance(self):
        return self.__balance

account = Account2("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print()

#==================================================================================
# REAL-LIFE EXAMPLE 3: SHOPPING CART
#==================================================================================

print("--- EXAMPLE 3: SHOPPING CART ---")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product):
        self.items.append(product)
        return f"Added {product.name}"
    
    def get_total(self):
        return sum(item.price for item in self.items)

cart = ShoppingCart()
cart.add_item(Product("Laptop", 999))
cart.add_item(Product("Mouse", 25))
print(f"Total: ${cart.get_total()}")
print()

#==================================================================================
# REAL-LIFE EXAMPLE 4: EMPLOYEE SYSTEM
#==================================================================================

print("--- EXAMPLE 4: EMPLOYEE SYSTEM ---")

class Employee4:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name} got raise of ${amount}"

class Manager(Employee4):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

manager = Manager("Bob", 8000, 5)
print(manager.give_raise(1000))
print(f"Manager: {manager.name}, Salary: ${manager.salary}, Team: {manager.team_size}")
print()

