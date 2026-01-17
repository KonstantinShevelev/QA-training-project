colors = ["red", "green", "blue", "yellow", "purple"]
print(colors)
print(colors[0])
print(colors[-1])
print(colors[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
numbers.insert(1,15)
print(numbers)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
comb = list_a + list_b
print(comb)
repeated_list = list_a *3
print(repeated_list)

print(f"3 in list_a? {3 in list_a}")