#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg, num = 1, number
if number < 0:
    num = number * -1
    neg = -1
num = num % 10
if (num * neg > 5):
    print("Last digit of {} is {} and is greater than 5"
          .format(number, num * neg))
elif (num * neg == 0):
    print("last digit of {} is {} and is 0".format(number, num * neg))
elif (num * neg < 6 and num * neg != 0):
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, num * neg))
