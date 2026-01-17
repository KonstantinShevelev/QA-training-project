choice  = input("Enter 1 - 3")

match choice:
    case '1':
        print("A option is chosen")
    case '2':
        print("B option is chosen")
    case '3':
        print("C option is chosen")
    case _:
        print("Unknown option")