lst = ['10', '20', '5', 'abc', '45']
summ =0
for i in range(len(lst)):
    try:
        summ += int(lst[i])

    except ValueError:
        print("data conversion error")
print(summ)


