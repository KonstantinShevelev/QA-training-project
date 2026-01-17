counter = 10
while True:

    print(counter)
    counter -= 1
    if counter == 5:
        print("Halfway is done")
        continue
    if counter == 0:
        print("Start!")
        break