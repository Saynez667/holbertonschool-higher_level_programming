# Python Inheritance

## Resources

Read or watch:

*   [Inheritance](https://realpython.com/inheritance-composition-python/)
*   [Multiple inheritance](https://realpython.com/multiple-inheritance-python/)
*   [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
*   [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=mn-1w2z0_9Y)

## Learning Objectives 🎯

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**

*   What is a superclass, baseclass or parentclass
*   What is a subclass
*   How to list all attributes and methods of a class or instance
*   When can an instance have new attributes
*   How to inherit class from another
*   How to define a class with multiple base classes
*   What is the default class every class inherit from
*   How to override a method or attribute inherited from the base class
*   Which attributes or methods are available by heritage to subclasses
*   What is the purpose of inheritance
*   What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Requirements

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

### Python Test Cases

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files should end with a new line
*   All your test files should be inside a folder `tests`
*   All your test files should be text files (extension: `.txt`)
*   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Documentation

*   Do not use the words `import` or `from` inside your comments, the checker will think you are trying to import some modules

## Tasks

### 0. Lookup (mandatory)

Write a function that returns the list of available attributes and methods of an object:

*   Prototype: `def lookup(obj):`
*   Returns a list object
*   You are not allowed to import any module

*   [File: 0-lookup.py](0-lookup.py)

### 1. My list (mandatory)

Write a class `MyList` that inherits from `list`:

*   Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
*   You can assume that all the elements of the list will be of type `int`
*   You are not allowed to import any module

*   [File: 1-my\_list.py](1-my_list.py), [tests/1-my\_list.txt](tests/1-my_list.txt)

### 2. Exact same object (mandatory)

Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

*   Prototype: `def is_same_class(obj, a_class):`
*   You are not allowed to import any module

*   [File: 2-is\_same\_class.py](2-is_same_class.py)

### 3. Same class or inherit from (mandatory)

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

*   Prototype: `def is_kind_of_class(obj, a_class):`
*   You are not allowed to import any module

*   [File: 3-is\_kind\_of\_class.py](3-is_kind_of_class.py)

### 4. Only sub class of (mandatory)

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

*   Prototype: `def inherits_from(obj, a_class):`
*   You are not allowed to import any module

*   [File: 4-inherits\_from.py](4-inherits_from.py)

### 5. Geometry module (mandatory)

Write an empty class `BaseGeometry`.

*   You are not allowed to import any module

*   [File: 5-base\_geometry.py](5-base_geometry.py)

### 6. Improve Geometry (mandatory)

Write a class `BaseGeometry` (based on 5-base\_geometry.py).

*   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
*   You are not allowed to import any module

*   [File: 6-base\_geometry.py](6-base_geometry.py)

### 7. Integer validator (mandatory)

Write a class `BaseGeometry` (based on 6-base\_geometry.py).

*   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
*   Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    *   you can assume `name` is always a string
    *   if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    *   if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
*   You are not allowed to import any module

*   [File: 7-base\_geometry.py](7-base_geometry.py), [tests/7-base\_geometry.txt](tests/7-base_geometry.txt)

### 8. Rectangle (mandatory)

Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py).

*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers, validated by `integer_validator`

*   [File: 8-rectangle.py](8-rectangle.py)

### 9. Full rectangle (mandatory)

Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py). (task based on 8-rectangle.py)

*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers validated by `integer_validator`
*   the `area()` method must be implemented
*   `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

*   [File: 9-rectangle.py](9-rectangle.py)

### 10. Square #1 (mandatory)

Write a class `Square` that inherits from `Rectangle` (9-rectangle.py):

*   Instantiation with `size`: `def __init__(self, size):`
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   the `area()` method must be implemented

*   [File: 10-square.py](10-square.py)

### 11. Square #2 (mandatory)

Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (task based on 10-square.py)

*   Instantiation with `size` and `x`, `y`: `def __init__(self, size, x=0, y=0):`
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   Public getter and setter `size`
*   Public getter and setter `x`
*   Public getter and setter `y`

*   [File: 11-square.py](11-square.py)

### 12. Rectangle #2

Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py). (task based on 9-rectangle.py)

*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers validated by `integer_validator`
*   Public getter and setter `width`
*   Public getter and setter `height`

*   [File: 12-rectangle.py](12-rectangle.py)

## Repository Structure 📁
```bash
python-inheritance/
├── 0-lookup.py
├── 1-my_list.py
├── 2-is_same_class.py
├── 3-is_kind_of_class.py
├── 4-inherits_from.py
├── 5-base_geometry.py
├── 6-base_geometry.py
├── 7-base_geometry.py
├── 8-rectangle.py
├── 9-rectangle.py
├── 10-square.py
├── 11-square.py
└── 12-rectangle.py
```

> GitHub repository: holbertonschool-higher\_level\_programming
> Directory: python-inheritance

## Authors
[Saynez667](https://github.com/Saynez667)