def format_user_data(**kwargs):
    # Функция принимает любое количество именованных аргументов и печатает их
    for key, value in kwargs.items():
        # Форматируем ключ для лучшей читаемости (например, 'user_name' -> 'User Name')
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

# Вызов функции с различными именованными аргументами
format_user_data(name="иван", age=30, city="казань")
print("-" * 10)
format_user_data(product_option="Молоко", price=75) # Другой набор данных