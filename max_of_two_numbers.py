def max_of_2(a, b):
    if a > b:
        return a
    elif b > a:
        return b


num1 = input("Please enter the first number")
num2 = input("Please enter the second number")
if num1 == num2:
    print("Both the numbers are equal")
else:
    maximum = max_of_2(num1, num2)
    print(f"{maximum} is the highest number")