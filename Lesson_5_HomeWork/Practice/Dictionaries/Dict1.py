grades = {'Math': 5, 'History': 4, 'Physics': 5, 'Literature': 4}
print("Keys:")
for key in grades:
    print(key)
print("\nValues:")
for value in grades.values():
    print(value)
print("\nPairs:")
for key, value in grades.items():
    print(f"{key}: {value}")

print(f"'Physics' is in the dict? {'Physics' in grades}")
print(f"'Chemistry' is in the dict? {'Chemistry' in grades}")
print(f"Amount of elements: {len(grades)}")