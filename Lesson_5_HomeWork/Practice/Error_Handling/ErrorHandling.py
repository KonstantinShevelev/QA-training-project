def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Zero division is impossible")
    return a/b

print(safe_divide(10,0))