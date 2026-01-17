counter = 0
while True:
    counter += 1

    if counter % 3 == 0:
        continue
        print(f"Пропускаем число {counter}")
    if counter == 10:
        print("Достигнуто 10, выходим!")
        break

    print(f"Текущий счетчик: {counter}")