#!/usr/bin/python3
import random
number = random.randint(-10, 10)
positive = (number > 0)
zero = (number == 0)
negative = (number < 0)
if positive:
    print(f"{number} is positive")
if zero:
    print(f"{number} is zero")
if negative:
    print(f"{number} is negative")
