cities = input().split()
for i in range(len(cities)):
    if 'a' in cities[i].lower():
        print(i + 1, cities[i], "(contains 'a')")
    else:
        print(i + 1, cities[i])

