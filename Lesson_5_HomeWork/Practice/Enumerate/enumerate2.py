lst = ['a', 'b', 'c']
# expected dict {0: 'a', 1: 'b', 2: 'c'}
dict = {}
for index, item in enumerate(lst):
    dict[index] = item
print(f"cea{dict}")