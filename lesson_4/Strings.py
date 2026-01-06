img = [[(0, 0, 0), (255, 255, 255)], [(255, 255, 255), (0, 0, 0)]]
copy_img = []

for row_idx in range(len(img)):
    row = []
    for col_idx in range(len(img[row_idx])):
        row.append(img[row_idx][col_idx])
    copy_img.append(row)

print("img =", img)
print("copy_img =", copy_img)
print("id of img =", id(img))
print("id of copy_img =", id(copy_img))