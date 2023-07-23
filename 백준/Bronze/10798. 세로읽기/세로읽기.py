mat = []
max_length = 15
row = 5
for _ in range(row):
    mat.append(input())

for c in range(max_length):
    for r in range(row):
        try:
            print(mat[r][c], end="")
        except:
            continue