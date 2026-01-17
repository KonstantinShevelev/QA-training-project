phrase = input("Enter a phrase\n")
vowels = "aeiou"
count_vowels = 0
for char in phrase:
    if char.lower() in vowels:
        count_vowels += 1
print(f"Amount of vowels: {count_vowels}")