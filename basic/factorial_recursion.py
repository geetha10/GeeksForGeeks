def factorial(num):
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)


num = input("Enter a number for finding factorial")
if num.isdigit():
    num = int(num)
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")
else:
    print("Please enter a valid Integer")
