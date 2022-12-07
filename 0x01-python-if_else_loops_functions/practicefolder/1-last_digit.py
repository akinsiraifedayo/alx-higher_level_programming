#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if (last_digit > 5):
	extra = "greater than 5"
if (last_digit == 0):
	extra = "0"
if (last_digit < 6 & last_digit > 0):
	extra = "and is less than 6 and not zero"
message = (f'Last digit of {number} is {last_digit} and is')
print("Last digit of ", number, " is ", last_digit,"and is ", extra)
