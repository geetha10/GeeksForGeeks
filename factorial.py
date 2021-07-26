def factorial(num):
    result = 1
    for x in range(1, num+1):
        result = result*x
    return result


num = input("Enter a number for finding factorial")
if num.isdigit():
    num = int(num)
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")
else:
    print("Please enter a valid Integer")
