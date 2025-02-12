# Square Class Project 📐

## Background Context 📚
In this project, you will practice **Object-Oriented Programming (OOP)** by implementing a series of classes that model the behavior of a square. OOP is a fundamental concept in software development, and this project will help you better understand the key concepts of **classes**, **objects**, **methods**, and **attributes**.

The goal is to deepen your understanding of:
- Classes and objects
- Instance attributes and methods
- Private vs. public attributes
- Property getters and setters
- Data validation using custom exceptions

By the end of this project, you should be able to explain OOP concepts clearly, design your own classes, and implement features like **data validation**, **encapsulation**, and **property management** in Python.

---

## Learning Objectives 🎯
At the end of this project, you should be able to:
- Understand Object-Oriented Programming (OOP) principles
- Create a class and instantiate it
- Work with public, private, and protected attributes
- Use the `__init__` method for class initialization
- Implement getter and setter methods for data encapsulation
- Create methods to compute attributes like the area of a square
- Implement logic for printing objects or formatting their output
- Handle exceptions for invalid data input

---

## Project Structure 🗂️
This project consists of the following tasks:

### Task 0: My first square 🟥
Define an empty class `Square` that defines a square.
- **File:** `0-square.py`

---

### Task 1: Square with size 🔲
Add a private instance attribute `size` to the `Square` class.
- **File:** `1-square.py`

---

### Task 2: Size validation ✅
Add validation to ensure the `size` attribute is an integer and greater than or equal to 0.
- **File:** `2-square.py`

---

### Task 3: Area of a square 🟦
Add a method `area()` that returns the area of the square (i.e., `size * size`).
- **File:** `3-square.py`

---

### Task 4: Access and update private attribute 🔐
Use Python's `property` and `setter` to manage the `size` attribute.
- **File:** `4-square.py`

---

### Task 5: Printing a square 🖼️
Implement a method `my_print()` that prints the square using the `#` character. If the size is 0, print an empty line.
- **File:** `5-square.py`

---

### Task 6: Coordinates of a square 📍
Extend the `Square` class to accept a `position` attribute, which controls the starting position of the square when printed (e.g., spaces before the square).
- **File:** `6-square.py`

---

## Requirements 📋

### General Requirements:
- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled using Python 3.8.5 on Ubuntu 20.04 LTS
- All files must end with a new line
- All files must be executable
- A README.md file is required in the root of the project folder
- All modules and functions must have proper docstrings
- Code must follow the PEP 8 style guide (`pycodestyle`, version 2.7.*)
- The length of files will be tested using `wc`

---

## Example 🖥️

Here’s an example of how you can use the Square class:
```python
#!/usr/bin/python3
Square = import('5-square').Square
my_square = Square(3)
my_square.my_print()
print("--")
my_square.size = 10
my_square.my_print()
print("--")
my_square.size = 0
my_square.my_print()
print("--")
```

### Output:
```bash
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
```

---

## Resources 📚

Here are some resources to help you complete this project:
1. [Object-Oriented Programming (OOP)](https://realpython.com/python3-object-oriented-programming/)
2. [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)
3. [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

---

## GitHub Repository 📍

You can find the code for this project on GitHub at the following location:

**GitHub Repository:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)  
**Directory:** `python-classes`

Each task has its corresponding file in the repository, so make sure to look for the appropriate file name and task description.
```bash
python-classes/
├── 0-square.py # Task 0: My first square
├── 1-square.py # Task 1: Square with size
├── 2-square.py # Task 2: Size validation
├── 3-square.py # Task 3: Area of a square
├── 4-square.py # Task 4: Access and update private attribute
├── 5-square.py # Task 5: Printing a square
└── 6-square.py # Task 6: Coordinates of a square
```
## Authors
[Saynez667](https://github.com/Saynez667)