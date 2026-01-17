data = [12,13,15]
match data:
    case int():
        print(f"{data} integer")
    case str():
        print(f"{data} string")
    case list():
        print(f"{data}: List")
    case _:
        print(f"{data}: Another type")