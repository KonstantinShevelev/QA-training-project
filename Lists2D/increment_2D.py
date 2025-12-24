def increment_2D(list_2d):
    new_2d = []
    for i in range(len(list_2d)):
        row = []
        for j in range(len(list_2d[i])):
           row.append(list_2d[i][j]+1)
        new_2d.append(row)
    return(new_2d)

list_2d=[[8,1,3],
         [2,3,4],
         [1,2,4]]

print(increment_2D(list_2d))