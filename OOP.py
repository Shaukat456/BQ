# Explain Classes in python with examples

# Classes are the blueprint for creating objects. They can contain methods and attributes that are associated with the object created from it.


# Example 1
class Cat:
    def __init__(self, providedname, providedage):
        self.name = providedname
        self.age = providedage
        self.height = "5'5"

    # def bark(self):
    #     print(f"{self.name} is barking")


cat1 = Cat("Tom", 5)


# Example 2
class Car:

    year = 2020

    def __init__(self, providedModel, providedAge):
        self.model = providedModel
        self.age = providedAge

    def drive(self):
        print(f"{self.model} is driving")


car1 = Car("Toyota", 5)


# Example 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")


p1 = Person("John", 25)
p1.walk()
# Explain constructor in python with examples

# A constructor is a special method in a class that is automatically called when an object is created. It is used to initialize the object's attributes.


# Example 1 with explanation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")


# In this example, the __init__ method is the constructor of the Dog class. It takes two parameters, name and age, and initializes the object's attributes self.name and self.age with the values passed to the constructor.


# Example 2 with explanation
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


# In this example, the __init__ method is the constructor of the Car class. It takes two parameters, model and year, and initializes the object's attributes self.model and self.year with the values passed to the constructor.


# now we can create objects from these classes

dog1 = Dog("Buddy", 5)
dog1.bark()


car1 = Car("Toyota", 2020)
car1.drive()


person1 = Person("John", 25)
person1.walk()

# Object contains state, identity and behavior

# Explain state ,identity and behavior of an object in python with examples


# State: The state of an object is the value of its attributes at a given time. For example, the state of a car object can be its model and year.

# Identity: The identity of an object is a unique identifier that distinguishes it from other objects. For example, two car objects with the same model and year are still different objects with different identities.

# Behavior: The behavior of an object is defined by its methods, which are functions that can be called on the object to perform certain actions. For example, a car object can have a drive method that allows it to drive.


# Example 1 explaining state, identity and behavior of an object
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


car1 = Car("Toyota", 2020)
car1.drive()

# State: The state of car1 object is model = "Toyota" and year = 2020
# Identity: The identity of car1 object is unique and different from other objects
# Behavior: The behavior of car1 object is to drive, which is defined by the drive method


# Class Attributes and Instance Attributes

# Explain class attributes and instance attributes in python with examples

# Class attributes are attributes that are shared by all instances of a class. They are defined outside the constructor and are accessed using the class name.

# Instance attributes are attributes that are specific to each instance of a class. They are defined inside the constructor and are accessed using the self keyword.


# Example 1 with explanation
class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


dog1 = Dog("Buddy", 5)


# In this example, species is a class attribute that is shared by all instances of the Dog class. name and age are instance attributes that are specific to each instance of the Dog class.


# Example 2 with explanation
class Car:
    wheels = 4  # class attribute

    def __init__(self, model, year):
        self.model = model  # instance attribute
        self.year = year  # instance attribute


# In this example, wheels is a class attribute that is shared by all instances of the Car class. model and year are instance attributes that are specific to each instance of the Car class.


# Method in python

# Explain method in python with examples

# A method is a function that is associated with a class and can be called on an object of that class. It can perform actions on the object or return values.


# Example 1 with explanation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")


dog1 = Dog("Buddy", 5)

dog1.bark()
# In this example, bark is a method of the Dog class. It takes no parameters (other than self, which is a reference to the object itself) and prints a message indicating that the dog is barking.


# Example 2 with explanation
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


# In this example, drive is a method of the Car class. It takes no parameters (other than self) and prints a message indicating that the car is driving.


# Inheritance in python

# Explain inheritance in python with examples


# Inheritance is a mechanism in which a new class inherits attributes and methods from an existing class. The existing class is called the base class or parent class, and the new class is called the derived class or child class.


# Example 1 with explanation
class Animal:
    def __init__(self, providedspecies):
        self.species = providedspecies

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog("Canis familiaris")
dog1.bark()

# In this example, Animal is the base class and Dog is the derived class. Dog inherits the attributes and methods of Animal, such as the species attribute and the eat method. It also defines its own method, bark.


# Example 2 with explanation
class Vehicle:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("Vehicle is driving")


class Car(Vehicle):

    def honk(self):
        print("Car is honking")


# In this example, Vehicle is the base class and Car is the derived class. Car inherits the attributes and methods of Vehicle, such as the model attribute and the drive method. It also defines its own method, honk.


# Polymorphism in python

# Explain polymorphism in python with examples

# Polymorphism is the ability of an object to take on different forms or behaviors depending on the context in which it is used. It allows objects of different classes to be treated as objects of a common superclass.


# Example 1 with explanation


class Animal:

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


class Cat(Animal):
    def speak(self):
        print("Cat is meowing")


# In this example, Animal is the base class with a speak method that does nothing. Dog and Cat are derived classes that override the speak method with their own implementations. This allows objects of type Dog and Cat to be treated as objects of type Animal.


# Example 2 with explanation
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# explain encapsulation in python with examples

# Encapsulation is the bundling of data and methods that operate on that data into a single unit, called a class. It allows the data to be hidden from the outside world and accessed only through the methods of the class.


# Example 1 with explanation


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


p1 = Person("John", 25)
print(p1.get_name())

# In this example, the name and age attributes of the Person class are encapsulated by making them private (using double underscores). The get_name and get_age methods provide controlled access to these attributes, allowing them to be accessed only through these methods.


# Example 2 with explanation


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")


# In this example, the account_number and balance attributes of the BankAccount class are encapsulated by making them private. The deposit and withdraw methods provide controlled access to these attributes, allowing deposits and withdrawals to be made only through these methods.


# Abstraction in python

# Explain abstraction in python with examples

# Abstraction is the process of hiding the implementation details of a class and exposing only the essential features to the outside world. It allows the user to interact with the class without needing to know how it is implemented.


# Example 1 with explanation
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
