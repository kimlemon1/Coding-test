mat = []
col = 9
row = 9
for _ in range(row):
    mat.append(list(map(int, input().split())))

max_val = mat[0][0]
max_idx = [0, 0]
for i in range(row):
    for j in range(col):
        if max_val < mat[i][j]:
            max_val = mat[i][j]
            max_idx = [i, j]
print(max_val)
print(max_idx[0]+1, max_idx[1]+1)