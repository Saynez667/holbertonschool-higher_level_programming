# python-data_structures

This project explores data structures in Python, focusing on lists and tuples.

## [Learning Objectives](pplx://action/followup)

By completing this project, you should be able to explain the following concepts without assistance:

### [General](pplx://action/followup)

*   What are lists and how to use them
*   What are the differences and similarities between strings and lists
*   What are the most common methods of lists and how to use them
*   How to use lists as stacks and queues
*   What are list comprehensions and how to use them
*   What are tuples and how to use them
*   When to use tuples versus lists
*   What is a sequence
*   What is tuple packing
*   What is sequence unpacking
*   What is the `del` statement and how to use it

## [Resources](pplx://action/followup)

*   [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
*   [Data structures (until 5.3. Tuples and Sequences included)](https://docs.python.org/3/tutorial/datastructures.html)
*   [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=N-dKz4CqiOU)

## [Requirements](pplx://action/followup)

### [Python Scripts](pplx://action/followup)

*   **[Allowed editors](pplx://action/followup):** `vi`, `vim`, `emacs`
*   **[Operating System](pplx://action/followup):** Ubuntu 20.04 LTS
*   Your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` (version 2.7.*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

## [Tasks](pplx://action/followup)

| Task                                                                                                 | Description                                                                                                                                                                                                                                                                                                      | File(s)                        |
| :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- |
| 0\. Print a list of integers                                                                         | Write a function that prints all integers of a list. `def print_list_integer(my_list=[]):` Format: one integer per line. You are not allowed to import any module. You can assume that the list only contains integers. You are not allowed to cast integers into strings. You have to use `str.format()` to print integers. | `0-print_list_integer.py`     |
| 1\. Secure access to an element in a list                                                            | Write a function that retrieves an element from a list. `def element_at(my_list, idx):` If `idx` is negative, the function should return `None`. If `idx` is out of range, the function should return `None`. You are not allowed to import any module. You are not allowed to use `try/except`.                          | `1-element_at.py`             |
| 2\. Replace element                                                                                  | Write a function that replaces an element of a list at a specific position. `def replace_in_list(my_list, idx, element):` If `idx` is negative, the function should not modify anything, and returns the original list. If `idx` is out of range, the function should not modify anything, and returns the original list. You are not allowed to import any module. You are not allowed to use `try/except`. | `2-replace_in_list.py`        |
| 3\. Print a list of integers... in reverse!                                                          | Write a function that prints all integers of a list, in reverse order. `def print_reversed_list_integer(my_list=[]):` Format: one integer per line. You are not allowed to import any module. You can assume that the list only contains integers. You are not allowed to cast integers into strings. You have to use `str.format()` to print integers. | `3-print_reversed_list_integer.py` |
| 4\. Replace in a copy                                                                                | Write a function that replaces an element in a list at a specific position without modifying the original list. `def new_in_list(my_list, idx, element):` If `idx` is negative, the function should return a copy of the original list. If `idx` is out of range, the function should return a copy of the original list. You are not allowed to import any module. You are not allowed to use `try/except`. | `4-new_in_list.py`            |
| 5\. Can you C me now?                                                                                 | Write a function that removes all characters `c` and `C` from a string. `def no_c(my_string):` The function should return the new string. You are not allowed to import any module. You are not allowed to use `str.replace()`.                                                                                                                                  | `5-no_c.py`                   |
| 6\. Lists of lists = Matrix                                                                          | Write a function that prints a matrix of integers. `def print_matrix_integer(matrix=[[]]):` Format: see example. You are not allowed to import any module. You can assume that the list only contains integers. You are not allowed to cast integers into strings. You have to use `str.format()` to print integers.            | `6-print_matrix_integer.py`    |
| 7\. Tuples addition                                                                                  | Write a function that adds 2 tuples. `def add_tuple(tuple_a=(), tuple_b=()):` Returns a tuple with 2 integers. If a tuple is smaller than 2, use the value 0 for each missing integer. If a tuple is bigger than 2, use only the first 2 integers. You are not allowed to import any module. You can assume that the two tuples will only contain integers.                               | `7-add_tuple.py`              |
| 8\. More returns!                                                                                    | Write a function that returns a tuple with the length of a string and its first character. `def multiple_returns(sentence):` If the sentence is empty, the first character should be equal to `None`. You are not allowed to import any module.                                                                                                             | `8-multiple_returns.py`        |
| 9\. Find the max                                                                                     | Write a function that finds the biggest integer of a list. `def max_integer(my_list=[]):` If the list is empty, return `None`. You can assume that the list only contains integers. You are not allowed to import any module. You are not allowed to use the builtin `max()`.                                                                                                  | `9-max_integer.py`            |
| 10\. Only by 2                                                                                       | Write a function that finds all multiples of 2 in a list. `def divisible_by_2(my_list=[]):` Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2. The new list should have the same size as the original list. You are not allowed to import any module.                                                       | `10-divisible_by_2.py`          |
| 11\. Delete at                                                                                       | Write a function that deletes the item at a specific position in a list. `def delete_at(my_list=[], idx=0):` If `idx` is negative or out of range, nothing changes (returns the same list). You are not allowed to use `pop()`. You are not allowed to import any module.                                                                                                                            | `11-delete_at.py`             |
| 12\. Switch                                                                                          | Complete the source code in order to switch value of `a` and `b`. Your code should be inserted where the comment is (line 4). Your program should be exactly 5 lines long.                                                                                                                                                                                                                            | `12-switch.py`                |

## [Repo](pplx://action/followup)

*   **[GitHub repository](pplx://action/followup):** holbertonschool-higher_level_programming
*   **[Directory](pplx://action/followup):** python-data_structures

## Authors
[Saynez667](https://github.com/Saynez667)
