lst = ['ОК', 'Ошибка', 'ОК', 'ОК', 'Ошибка', 'Warning']
new_lst = []
for index, item in enumerate(lst):
    if item == 'Ошибка':
        new_lst.append(index)
print(new_lst)