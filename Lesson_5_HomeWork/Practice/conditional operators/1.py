user_input = input()
display_name = user_input if user_input is not None and user_input.strip() != "" else "Гость"

print(f"Ввод {repr(user_input)}, отображаемое имя: {display_name}")