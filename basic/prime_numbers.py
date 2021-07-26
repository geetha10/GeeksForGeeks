start = input("Enter the start range")
end = input("Enter the end range")
if start.isdigit() and end.isdigit():
    start = int(start)
    end = int(end)
    for x in range(start, end + 1):
        if x > 1:
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                print(x)
