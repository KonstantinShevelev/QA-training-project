tup = ("Master and Margaritha", "Mikhail Bulgakov", "1996")
title, author, year = tup
print(f"Title of the book: {title}\nYear of establishing : {year}")
try:
    tup[2] = input("Try to change the year...\n")
except TypeError:
    print("Tuples are immutable, so it is not possible to directly modify an element of a tuple.")