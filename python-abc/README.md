# Python OOP - Abstract Class, Interface, Subclassing 🐍💡

## Introduction 📘

Welcome to this set of exercises designed to help you master Object-Oriented Programming (OOP) principles in Python. In this series, you will explore abstract classes, interfaces, duck typing, subclassing standard Python classes, and more. By completing these tasks, you'll be well-equipped to write clean, efficient, and reusable Python code using OOP techniques.

The exercises will guide you through the fundamentals, giving you hands-on experience in applying these concepts to real-world problems. Let's dive into Python OOP with a focus on:

- Abstract Classes & Interfaces: Learn to define common interfaces and enforce class contracts.
- Duck Typing: Understand how to write flexible, adaptable code using Python's dynamic typing.
- Subclassing: Build on standard Python classes to create custom data structures and functionality.
- Method Overriding: Customize and extend base class behaviors to suit your needs.
- Multiple Inheritance: Explore complex class relationships by inheriting from multiple base classes.
- Mixins: Write reusable classes that provide specific functionality to other classes.

## Learning Objectives 🎯

By the end of these exercises, you'll be able to:

- Create abstract classes to provide a template for subclasses and enforce a specific interface.
- Use abstract base classes to define interfaces and leverage duck typing to allow flexible method calls on objects.
- Inherit from built-in Python classes like list and dict to create specialized behaviors.
- Override methods in subclasses to customize inherited behavior.
- Master multiple inheritance and manage method resolution order (MRO).
- Use mixins to compose functionality from different classes without deep inheritance hierarchies.

## Resources 📚

- [Python 3 Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python ABC Documentation](https://docs.python.org/3/library/abc.html)
- [Real Python - Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [Sentdex - Python OOP Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)

These resources include articles, videos, and interactive tutorials to solidify your understanding of OOP.

## Tasks Overview 📝

### 0. Abstract Animal Class and its Subclasses

**Background:**
Learn to define and use abstract base classes (ABCs) in Python. Abstract classes ensure that derived classes implement specific methods, creating a common interface.

**Objective:**
- Create an abstract Animal class with an abstract sound() method.
- Implement two subclasses (Dog and Cat) that override the sound() method.

**Resources:**
- [Python ABC documentation](https://docs.python.org/3/library/abc.html)

### 1. Shapes, Interfaces, and Duck Typing

**Background:**
In this task, you'll combine abstract classes and duck typing to handle different shapes in a uniform way.

**Objective:**
- Create a Shape abstract class with methods for area() and perimeter().
- Implement Circle and Rectangle classes.
- Use duck typing to handle shapes generically in a shape_info() function.

**Resources:**
- [Duck Typing in Python](https://realpython.com/lessons/duck-typing/)

### 2. Extending the Python List with Notifications

**Background:**
Learn how to extend Python's built-in list class to add custom behavior. This is useful when you want to modify or extend the functionality of standard Python types.

**Objective:**
- Create a VerboseList that extends the list class.
- Override methods like append(), extend(), remove(), and pop() to print notifications.

**Testing:**
Test all methods and ensure the appropriate messages are printed after each list modification.

### 3. CountedIterator - Keeping Track of Iteration

**Background:**
Understand how to extend Python's iterator protocol by adding additional functionality, such as counting the number of iterations.

**Objective:**
- Create a CountedIterator class that keeps track of the number of items it has iterated over.
- Override the __next__() method to increment the count.

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance

**Background:**
Learn about multiple inheritance and method resolution order (MRO). Multiple inheritance allows a class to inherit attributes and methods from more than one parent class.

**Objective:**
- Create Fish and Bird classes with basic behaviors like swim() and fly().
- Implement a FlyingFish class that inherits from both Fish and Bird, and override their methods.

**Investigate MRO:**
Use mro() or .__mro__ to explore the method resolution order of FlyingFish.

### 5. The Mystical Dragon - Mastering Mixins

**Background:**
Mixins allow you to add specific functionality to classes without deep inheritance hierarchies.

**Objective:**
- Create two mixins (SwimMixin and FlyMixin), each providing swim() and fly() methods.
- Design a Dragon class that inherits from both mixins.

**Testing:**
Instantiate a Dragon object and demonstrate its ability to swim, fly, and roar (if implemented).

## Example Output 💻

### 0. Abstract Animal Class
```bash
Bobby says: Bark
Garfield says: Meow
```

### 1. Shapes, Interfaces, and Duck Typing
```bash
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

### 2. VerboseList Notifications
```bash
Added4 to the list.
Extended the list with2 items.
Removed2 from the list.
Popped6 from the list.
Popped1 from the list.
```

### 3. CountedIterator
```bash
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

### 4. FlyingFish
```bash
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```
### 5. Dragon Mixins
```bash
The creature swims!
The creature flies!
The dragon roars!
```
## Authors
[Saynez667](https://github.com/Saynez667)