# python-exceptions

This project focuses on understanding and handling exceptions in Python. It covers safe printing of lists and integers, and how to handle different types of exceptions.

## Learning Objectives

By completing this project, you should be able to explain the following concepts without assistance:

### General

*   Why Python programming is awesome
*   What’s the difference between errors and exceptions
*   What are exceptions and how to use them
*   When do we need to use exceptions
*   How to correctly handle an exception
*   What’s the purpose of catching exceptions
*   How to raise a built-in exception
*   When do we need to implement a clean-up action after an exception

## Resources

*   [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
*   [Learn to Program 11 Static & Exception Handling (starting at minute 7)](https://www.youtube.com/watch?v=hWxszZ9vc-o)

## Requirements

### General

*   **Allowed editors:** `vi`, `vim`, `emacs`
*   **Operating System:** Ubuntu 20.04 LTS
*   **Python Version:** python3 (version 3.8.5)
*   All files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` (version 2.7.*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

## Tasks

| Task                                                          | Description                                                                                                                                                                                                                                                                                                                                      | File(s)                      |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
| 0\. Safe list printing                                        | Write a function that prints `x` elements of a list.  `def safe_print_list(my_list=[], x=0):` `my_list` can contain any type (integer, string, etc.). All elements must be printed on the same line followed by a new line. `x` represents the number of elements to print. `x` can be bigger than the length of `my_list`. Returns the real number of elements printed. You have to use `try: / except:`. You are not allowed to import any module. You are not allowed to use `len()`. | `0-safe_print_list.py`         |
| 1\. Safe printing of an integers list                        | Write a function that prints an integer with "{:d}".format(). `def safe_print_integer(value):` `value` can be any type (integer, string, etc.). The integer should be printed followed by a new line. Returns `True` if value has been correctly printed (it means the value is an integer). Otherwise, returns `False`. You have to use `try: / except:`. You have to use `"{:d}".format()` to print as integer. You are not allowed to import any module. You are not allowed to use `type()`.                                                                                                    | `1-safe_print_integer.py`      |
| 2\. Print and count integers                                 | Write a function that prints the first `x` elements of a list and *only* integers. `def safe_print_list_integers(my_list=[], x=0):` `my_list` can contain any type (integer, string, etc.). All integers have to be printed on the same line followed by a new line - other types of value in the list must be skipped (in silence). `x` represents the number of elements to access in `my_list`. `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur. Returns the real number of integers printed. You have to use `try: / except:`. You have to use `"{:d}".format()` to print an integer. You are not allowed to import any module. You are not allowed to use `len()`. | `2-safe_print_list_integers.py` |
| 3\. Integers division with debug                             | Write a function that divides 2 integers and prints the result. `def safe_print_division(a, b):`  You can assume that `a` and `b` are integers. The result of the division should print on the `finally:` section, preceded by `Inside result:`. Returns the value of the division, otherwise: `None`. You have to use `try: / except: / finally:`. You have to use `"{}".format()` to print the result. You are not allowed to import any module.                                                                                                | `3-safe_print_division.py`     |
| 4\. Divide a list                                             | Write a function that divides element by element 2 lists. `def list_division(my_list_1, my_list_2, list_length):`  `my_list_1` and `my_list_2` can contain any type (integer, string, etc.). `list_length` can be bigger than the length of both lists. Returns a new list (`length = list_length`) with all divisions. If 2 elements can’t be divided, the division result should be equal to 0. If an element is not an integer or float, print: `wrong type`. If the division can’t be done (`/0`), print: `division by 0`. If `my_list_1` or `my_list_2` is too short, print: `out of range`. You have to use `try: / except: / finally:`. You are not allowed to import any module. | `4-list_division.py`           |
| 5\. Raise exception                                           | Write a function that raises a type exception. `def raise_exception():` You are not allowed to import any module.                                                                                                                                                                                                                                                                                               | `5-raise_exception.py`         |
| 6\. Raise a message                                           | Write a function that raises a name exception with a message. `def raise_exception_msg(message=""):` You are not allowed to import any module.                                                                                                                                                                                                                                                                                           | `6-raise_exception_msg.py`     |

## Repo

*   **GitHub repository:** [holbertonschool-higher\_level\_programming](https://github.com/holbertonschool/holbertonschool-higher_level_programming)
*   **Directory:** python-exceptions

## Authors
[Saynez667](https://github.com/Saynez667)
