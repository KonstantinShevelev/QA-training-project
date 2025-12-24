grades = map(int, input("Enter 3 grades:").split())
lst = list (grades)
a = lst[0] + lst[1] * lst[2]
b = lst[0] * (lst[1] + lst[2])
c = lst[0] * lst[1] * lst[2]
d = (lst[0] + lst[1]) * lst[2]
print(max(a,b,c,d))