"""
Python Program for n-th Fibonacci number

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

Fn = Fn-1 + Fn-2
With seed values

F0 = 0 and F1 = 1.
"""
import ast


def fibonacci_generator(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


try:
    nth_num = ast.literal_eval(input("Enter n"))
    if nth_num <= 0:
        print("Enter a valid input")
    else:
        nth_fibonacci_num = fibonacci_generator(nth_num)
    print(nth_fibonacci_num)
except Exception as error:
    print("Please enter a Integer", error)
