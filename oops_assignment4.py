# Q4) Write a Python program to implement abstraction using the following:
# Abstract Class: Shape (use ABC from abc module)
# Abstract Methods:
# area() → calculates the area of the shape
# perimeter() → calculates the perimeter of the shape
# Class: Circle (inherits from Shape)
# Attribute: radius
# Implements area() → returns π × radius²
# Implements perimeter() → returns 2 × π × radius
# Class: Rectangle (inherits from Shape)
# Attributes: length, width
# Implements area() → returns length × width
# Implements perimeter() → returns 2 × (length + width)
# Create objects of Circle, Rectangle and print their area and perimeter.
# Demonstrate abstraction because Shape cannot be instantiated directly, but all derived classes implement the abstract methods.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius**2
    def perimeter(self):
        return 2 * 3.14 * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length *self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
obj=Circle(4)
print(obj.area())
print(obj.perimeter())
obj2=Rectangle(3,4)
print(obj2.area())
print(obj2.perimeter())




