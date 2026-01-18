my_list = list(range(1,21))
#odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
cubed_nums = list(map(lambda x: x**3, filter(lambda x: x % 2 != 0, my_list)))
print(cubed_nums)