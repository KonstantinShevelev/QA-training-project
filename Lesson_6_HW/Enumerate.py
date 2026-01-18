inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']
processed_items = []
vowels = ('a', 'e', 'i', 'o', 'u')
for index, item in enumerate(inventory, start=1):
    if index % 2 == 0:
        if len(item) > 5:
            processed_items.append(f"{index}. Удлиненный {item}")
        else:
            processed_items.append(f"{index}. {item}")
    else:
        if item.startswith(vowels):
            processed_items.append(f"{index}.Стартует с гласной: {item}")
        else:
            processed_items.append(f"{index}. {item}")
print(inventory)
print(processed_items)
