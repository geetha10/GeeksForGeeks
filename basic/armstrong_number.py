def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
        print(x)
    print(f"order {n}")
    return n


def armstrong_num(x, n):
    sum = 0
    while x != 0:
        digit = x % 10
        x = x // 10
        power_digit_order_n = pow(digit, n)
        print(f"Digit {digit} and power {power_digit_order_n}")
        sum = sum + power_digit_order_n
    return sum


num = input("Enter a number to check if it is Armstrong number or not")
if num.isdigit():
    num = int(num)
    order_num = order(num)
    armstrong_sum = armstrong_num(num, order_num)
    if num == armstrong_sum:
        print("given number is a armstrong number")
    else:
        print("given number is not a armstrong number")
