#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
