# Python Inheritance

## Resources

*   [Inheritance](https://realpython.com/inheritance-composition-python/)
*   [Multiple inheritance](https://realpython.com/multiple-inheritance-python/)
*   [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
*   [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=mn-1w2z0_9Y)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

*   Superclass, baseclass, or parentclass
*   Subclass
*   Listing attributes and methods of a class or instance
*   Adding new attributes to instances
*   Inheriting from another class
*   Defining classes with multiple base classes
*   The default class every class inherits from
*   Overriding inherited methods or attributes
*   Available attributes/methods via inheritance
*   Purpose of inheritance
*   Usage of `isinstance`, `issubclass`, `type`, and `super`

## Requirements

### Python Scripts

*   **Editors:** `vi`, `vim`, `emacs`
*   **Environment:** Ubuntu 20.04 LTS, Python 3.8.5
*   **First line:** `#!/usr/bin/python3`
*   **Style:** `pycodestyle` (version 2.7.\*)
*   All files must be executable.
*   All files must end with a new line.
*   A `README.md` file is mandatory.

### Python Test Cases

*   **Editors:** `vi`, `vim`, `emacs`
*   **Location:** `tests` directory
*   **Format:** `.txt` files
*   **Execution:** `python3 -m doctest ./tests/*`
*   All modules, classes, and functions must have docstrings.  Docstrings should be descriptive sentences.
*   Collaboration on test cases is encouraged.

### Documentation

*   Do not use `import` or `from` in comments.

## Tasks

Each task is detailed below, including file names and a brief description.

**0. Lookup (mandatory)**

*   Write a function that returns the list of available attributes and methods of an object.
*   Prototype: `def lookup(obj):`
*   Returns a list.
*   No imports allowed.
*   File: `0-lookup.py`

**1. My list (mandatory)**

*   Write a class `MyList` that inherits from `list`.
*   Public instance method: `def print_sorted(self):` (prints the sorted list)
*   Assume all elements are integers.
*   No imports allowed.
*   Files: `1-my_list.py`, `tests/1-my_list.txt`

**2. Exact same object (mandatory)**

*   Write a function that returns `True` if the object is exactly an instance of the specified class, otherwise `False`.
*   Prototype: `def is_same_class(obj, a_class):`
*   No imports allowed.
*   File: `2-is_same_class.py`

**3. Same class or inherit from (mandatory)**

*   Write a function that returns `True` if the object is an instance of, or an instance of a class that inherited from, the specified class; otherwise `False`.
*   Prototype: `def is_kind_of_class(obj, a_class):`
*   No imports allowed.
*   File: `3-is_kind_of_class.py`

**4. Only sub class of (mandatory)**

*   Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.
*   Prototype: `def inherits_from(obj, a_class):`
*   No imports allowed.
*   File: `4-inherits_from.py`

**5. Geometry module (mandatory)**

*   Write an empty class `BaseGeometry`.
*   No imports allowed.
*   File: `5-base_geometry.py`

**6. Improve Geometry (mandatory)**

*   Write a class `BaseGeometry` (based on 5-base\_geometry.py).
*   Public instance method: `def area(self):` (raises an `Exception` with the message `area() is not implemented`)
*   No imports allowed.
*   File: `6-base_geometry.py`

**7. Integer validator (mandatory)**

*   Write a class `BaseGeometry` (based on 6-base\_geometry.py).
*   Public instance method: `def area(self):` (raises an `Exception`)
*   Public instance method: `def integer_validator(self, name, value):` (validates `value`)
    *   `name` is always a string
    *   If `value` is not an integer: raise a `TypeError` exception, with the message ``<name> must be an integer``
    *   If `value` is less or equal to 0: raise a `ValueError` exception with the message ``<name> must be greater than 0``
*   No imports allowed.
*   Files: `7-base_geometry.py`, `tests/7-base_geometry.txt`

**8. Rectangle (mandatory)**

*   Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py).
*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter.
    *   `width` and `height` must be positive integers, validated by `integer_validator`.
*   File: `8-rectangle.py`

**9. Full rectangle (mandatory)**

*   Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py). (Based on 8-rectangle.py)
*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers validated by `integer_validator`
*   Implement the `area()` method.
*   `print()` should print, and `str()` should return the following rectangle description: `[Rectangle] <width>/<height>`
*   File: `9-rectangle.py`

**10. Square #1 (mandatory)**

*   Write a class `Square` that inherits from `Rectangle` (9-rectangle.py).
*   Instantiation with `size`: `def __init__(self, size):`
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   Implement the `area()` method.
*   File: `10-square.py`

**11. Square #2 (mandatory)**

*   Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (Based on 10-square.py)
*   Instantiation with `size` and `x`, `y`: `def __init__(self, size, x=0, y=0):`
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   Public getter and setter for `size`
*   Public getter and setter for `x`
*   Public getter and setter for `y`
*   File: `11-square.py`

**12. Rectangle #2**

*   Write a class `Rectangle` that inherits from `BaseGeometry` (7-base\_geometry.py). (Based on 9-rectangle.py)
*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers validated by `integer_validator`
*   Public getter and setter for `width`
*   Public getter and setter for `height`
*   File: `12-rectangle.py`

## Repository Structure
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
└── tests/
└── 7-base_geometry.txt
```

*   GitHub repository: holbertonschool-higher\_level\_programming
*   Directory: python-inheritance

## Authors
[Saynez667](https://github.com/Saynez667)