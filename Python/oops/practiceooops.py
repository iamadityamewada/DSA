class Dog:
    def _init_(self, name):
        self.name = name
    
    def bark(self):
        print("Woof!")


dog = Dog("Max")
dog.bark()

# Constructor Practice

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
book1.display_info()
book2.display_info()



# Accessing and Modifying Object Attributes

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def celebrate_birthday(self):
        self.age += 1


person = Person("John", 30)
print(f"Initial age: {person.age}")
person.celebrate_birthday()
print(f"Updated age: {person.age}")




class Car:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("The car has started")


car = Car("Toyota", "Corolla", 2020)
car.start()


# Object Comparison

class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 3)
if rect1.area() > rect2.area():
    print("Rectangle 1 has a larger area")
else:
    print("Rectangle 2 has a larger area")


# Simple Inheritance Example

class Animal:
    def make_sound(self):
        print("Some sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Create objects and call method
animal = Animal()
cat = Cat()
animal.make_sound()
cat.make_sound()



# Constructor in Inheritance

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def _init_(self, name, age, salary):
        super()._init_(name, age)
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# Create object and call method
employee = Employee("Alice", 28, 50000)
employee.display_info()


# Overriding Methods

class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")

# Create objects and call method
vehicle = Vehicle()
car = Car()
vehicle.move()
car.move()
