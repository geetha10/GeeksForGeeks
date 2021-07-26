import ast


def simple_interest(p, t, r):
    return (p * t * r) / 100


try:
    principle = ast.literal_eval(input("Enter the Amount"))
    rate = ast.literal_eval(input("Enter the interest rate"))
    time = ast.literal_eval(input("Enter the time"))
except Exception as error:
    print("Your input cannot be parsed:", error)
else:
    interest = simple_interest(int(principle), int(time), int(rate))
    total = principle + interest
    print(f"Interest fo {principle} with rate {rate} for {time} time is {interest} and total to be paid is {total}")

