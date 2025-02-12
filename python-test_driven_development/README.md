# python-test_driven_development

This project focuses on understanding and implementing test-driven development (TDD) principles in Python. It covers writing documentation, implementing unit tests and doctests, and handling edge cases.

**[Important Notice](pplx://action/followup):** Starting today, write documentation and tests first, *before* coding.  The intranet checks for this project will only be released *after* the deadline, to encourage TDD. Collaborate on test cases but implement them individually.  Always consider edge cases.

## [Learning Objectives](pplx://action/followup)

By completing this project, you should be able to explain the following concepts without assistance:

### [General](pplx://action/followup)

*   Why Python programming is awesome
*   What an interactive test is
*   Why tests are important
*   How to write Docstrings to create tests
*   How to write documentation for each module and function
*   What the basic option flags are to create tests
*   How to find edge cases

## [Requirements](pplx://action/followup)

### [Python Scripts](pplx://action/followup)

*   **[Allowed editors](pplx://action/followup):** `vi`, `vim`, `emacs`
*   **[Operating System](pplx://action/followup):** Ubuntu 20.04 LTS
*   **[Python Version](pplx://action/followup):** python3 (version 3.8.5)
*   All files must end with a new line
*   The first line of all files should be exactly: `#!/usr/bin/python3`
*   A `README.md` file is mandatory at the root of the project folder.
*   Code should adhere to `pycodestyle` (version 2.7.*).
*   All files must be executable
*   The length of your files will be tested using `wc`

### [Python Test Cases](pplx://action/followup)

*   **[Allowed editors](pplx://action/followup):** `vi`, `vim`, `emacs`
*   All files must end with a new line
*   All test files should be inside a folder named `tests`
*   All test files should be text files with the extension `.txt` (for doctests) or `.py` (for unittests)
*   Tests should be executed using:
    *   Doctests: `python3 -m doctest ./tests/*`
    *   Unittests: `python3 -m unittest tests.6-max_integer_test`
*   All modules should have documentation (using docstrings): `python3 -c 'print(__import__("my_module").__doc__)'`
*   All functions should have documentation (using docstrings): `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   Documentation should be descriptive and explain the purpose of the module, class, or method.  The length of documentation *will* be checked.
*   Collaboration on test cases is encouraged to identify edge cases, but implementation should be individual.
*   The Checker will verify the presence of tests!

## [Tasks](pplx://action/followup)

| Task                                                          | Description                                                                                                                                                                                                                           | File(s)                                  |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------- |
| 0\. Integers addition                                         | Write a function that adds 2 integers. `def add_integer(a, b=98):` a and b must be integers or floats.  Raise a TypeError if not. Cast to integers if they are floats.  Returns an integer. No imports allowed.                 | `0-add_integer.py`, `tests/0-add_integer.txt` |
| 1\. Divide a matrix                                           | Write a function that divides all elements of a matrix. `def matrix_divided(matrix, div):` matrix must be a list of lists of integers or floats. Each row of the matrix must be the same size. div must be a number.  div can’t be equal to 0.  Elements should be rounded to 2 decimal places. Returns a new matrix. No imports allowed.                                                                                                                                                              | `2-matrix_divided.py`, `tests/2-matrix_divided.txt`|
| 2\. Say my name                                               | Write a function that prints `My name is <first name> <last name>`. `def say_my_name(first_name, last_name=""):` first\_name and last\_name must be strings. Raise a TypeError if not. No imports allowed.                                                                                                                                                                 | `3-say_my_name.py`, `tests/3-say_my_name.txt`|
| 3\. Print square                                              | Write a function that prints a square with the character `#`. `def print_square(size):` size is the size length of the square. size must be an integer. If size is less than 0, raise a ValueError. If size is a float and is less than 0, raise a TypeError. No imports allowed.                                                                                                                                                          | `4-print_square.py`, `tests/4-print_square.txt` |
| 4\. Text indentation                                          | Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`. `def text_indentation(text):` text must be a string. Raise a TypeError if not. No space at the beginning or at the end of each printed line. No imports allowed.                                                                                                                                    | `5-text_indentation.py`, `tests/5-text_indentation.txt` |
| 5\. Max integer - Unittest                                    | Write unittests for the function `def max_integer(list=[]):`.  Use the `unittest` module. Your test file should be a python file (`.py`) inside the `tests` folder.  `python3 -m unittest tests.6-max_integer_test`                                                                                                                                                                     | `6-max_integer.py`, `tests/6-max_integer_test.py` |

## [Repo](pplx://action/followup)

*   **[GitHub repository](pplx://action/followup):** [holbertonschool-higher\_level\_programming](https://github.com/holbertonschool/holbertonschool-higher_level_programming)
*   **[Directory](pplx://action/followup):** python-test\_driven\_development

## Authors
[Saynez667](https://github.com/Saynez667)
