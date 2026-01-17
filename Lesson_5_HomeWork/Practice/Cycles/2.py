phrase = input("Введите любое предложение...\n")
lst = phrase.split()
for word in lst:
    print (f"Слово: {word}, длина: {len(word)}")
