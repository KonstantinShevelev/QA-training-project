age = int(input("Enter the age: "))
if 0 < age <= 12:
    print("Child")
elif 13 < age <= 17:
    print("teenager")
elif 18 < age <= 64:
    print("adult")
elif 65 < age < 120:
    print("old")
else:
    print("Invalid age")