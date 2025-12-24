pencil = 3
pen = pencil + 2
marker = pen + 7

x,y,z = map(int, input().split())
print(pencil * x + pen * y + marker * z)