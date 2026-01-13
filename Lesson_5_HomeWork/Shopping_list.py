Shopping_list = ["молоко", "хлеб", "яйца", "сыр", "масло"]
Shopping_list.append("сок")
Shopping_list.insert(1,"йогурт")
Shopping_list[2] = "батон"
Shopping_list.remove("масло")
print(Shopping_list[0], Shopping_list[-1])
print(Shopping_list[1:4])
Shopping_list.sort()
print(Shopping_list)
print("Длина спсика покупок: ", len(Shopping_list))
