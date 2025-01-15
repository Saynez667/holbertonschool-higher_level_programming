#!/usr/bin/python3
import random
number = random.randint(-10, 10)
positive = (number>0)
zero = (number==0)
negative = (number<0)
if positive:
	print("is positive")
if zero:
	print("is zero")
if negative:
	print("is negative")
