num = int(input("Enter a number: "))

if num < 0:
    print("This is negative number")
else:
    size = "big " if num > 100 else ""
    parity = "even" if num % 2 == 0 else "odd"
    print(f"This is {size}{parity} number")
