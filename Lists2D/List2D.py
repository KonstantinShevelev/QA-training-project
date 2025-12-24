list_2D = [[0,1,2],
           [3,4,5],
           [6,7,8]]

total = 0
for i in range(len(list_2D)):
    for j in range(len(list_2D[i])):
        total += list_2D[i][j]

print(total)