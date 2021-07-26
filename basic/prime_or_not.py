"""
Python program to check whether a number is Prime or not
Difficulty Level : Easy
Last Updated : 12 Jul, 2021
Given a positive integer N, The task is to write a Python program to check if the number is prime or not.
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.
"""

import ast
try:
    num = ast.literal_eval(input("Enter a number to check whether it is Prime or not"))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
except Exception as error:
    print("Your input cannot be parsed. Please enter a Integer", error)
