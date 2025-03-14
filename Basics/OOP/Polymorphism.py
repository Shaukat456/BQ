# **Polymorphism in Python (With Real-World Analogies & Use Cases)**
#
# ## **What is Polymorphism?**
# Polymorphism means **"many forms."** It allows different classes to use the **same method name** but implement it differently.
#
# ✅ **Key Idea:** The same function/method works differently depending on the object that calls it.
#
# ---
#
# ## **Real-World Analogy**
# ### 🎵 **Musical Instrument Example**
# Imagine you go to a **music store** and ask different instruments to "play."
#
# - A **Guitar** will play by strumming strings.
# - A **Piano** will play by pressing keys.
# - A **Drum** will play by hitting the surface.
#
# Even though they all respond to "play," they behave **differently** based on their type.
#
# ---
#
# ## **Polymorphism in Python**
# ### **1️⃣ Method Overriding (Polymorphism in Inheritance)**
# When a **child class** provides a **specific implementation** of a method that is already defined in the **parent class**.
#
# #### **Example: Animals Making Sounds**
class Animal:
    def speak(self):
        return "Animals make sounds"


class Dog(Animal):
    def speak(self):  # Overriding the parent method
        return "Woof! Woof!"


class Cat(Animal):
    def speak(self):  # Overriding the parent method
        return "Meow! Meow!"


# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Different output for each class


# ### **Output:**
# ```
# Woof! Woof!
# Meow! Meow!
# ```
# **Explanation:**
# - The `speak()` method is defined in the `Animal` class but **overridden** in `Dog` and `Cat`.
# - When we call `speak()`, Python automatically calls the correct version based on the object type.
#
# ---
#
# ### **2️⃣ Method Overloading (Polymorphism with Functions)**
# Python **does not support traditional method overloading** like Java or C++, but we can achieve it using **default parameters** or `*args`.
#
# #### **Example: Calculator with Different Inputs**
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c  # Supports two or three arguments


calc = Calculator()
print(calc.add(2, 3))  # 2 arguments
print(calc.add(2, 3, 4))  # 3 arguments


# ### **Output:**
# ```
# 5
# 9
# ```
# **Explanation:**
# - The same `add()` function works with **two or three numbers** because of the **default value of `c`**.
#
# ---
#
# ### **3️⃣ Polymorphism with Functions**
# A function can use different objects that share a common method name.
#
# #### **Example: Vehicles Moving**
class Car:
    def move(self):
        return "The car is driving on the road"


class Boat:
    def move(self):
        return "The boat is sailing in water"


class Plane:
    def move(self):
        return "The plane is flying in the sky"


# Function that works with multiple classes
def transport(vehicle):
    print(vehicle.move())


# Calling function with different objects
transport(Car())  # Car object
transport(Boat())  # Boat object
transport(Plane())  # Plane object

# ### **Output:**
# ```
# The car is driving on the road
# The boat is sailing in water
# The plane is flying in the sky
# ```
# **Explanation:**
# - The `transport()` function works with **Car, Boat, and Plane**, even though they are different classes.
# - Python calls the **correct `move()` method** based on the object type.
#
# ---
#
# ## **4️⃣ Polymorphism with Abstract Classes (Using `ABC`)**
# If you want to **force** child classes to implement a method, you can use **abstract classes**.
#
# #### **Example: Shapes with Area Calculation**
from abc import ABC, abstractmethod


class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # Must be implemented in child classes


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Implementing the abstract method
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Implementing the abstract method
        return self.side * self.side


# Using polymorphism
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# ### **Output:**
# ```
# Area: 78.5
# Area: 16
# ```
# **Explanation:**
# - `Shape` is an **abstract class** with an **abstract method `area()`**.
# - `Circle` and `Square` **must** implement `area()`, ensuring consistency.
# - The same method `area()` behaves differently for different shapes.
#
# ---
#
# ## **Real-World Use Cases of Polymorphism**
# ✅ **Django/Flask Web Development:**
# - Different models (`User`, `Admin`, `Guest`) implement a `get_role()` method but return different roles.
#
# ✅ **Game Development:**
# - Different characters (`Player`, `Enemy`, `NPC`) have an `attack()` method, but each performs different actions.
#
# ✅ **Machine Learning & Data Science:**
# - A `train()` method behaves differently for `LinearRegression`, `DecisionTree`, and `NeuralNetwork` models.
#
# ✅ **E-commerce Applications:**
# - A `calculate_discount()` method in `Product` works differently for `Electronics`, `Clothing`, and `Books`.
#
# ## **Conclusion**
# Polymorphism allows **flexibility, reusability, and clean code.** It ensures that **objects of different types** can be handled **uniformly** without breaking functionality. 🚀
