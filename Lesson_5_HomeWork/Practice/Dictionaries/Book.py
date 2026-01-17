book = dict(title="War and Peace", author="Lev Toltoy", year=1869, genre="novel")
print(f"Словарь с dict(): {book}")
print(book["author"])
book["year"] = 1867
book['pages'] = 1225
print(book)
del book['genre']
print(f"Удаляем pages... {book.pop('pages')}")
print(f"Словарь после pop(): {book}")