N, M = map(int, input().split())
mat1 = []
mat2 = []
for _ in range(N):
    mat1.append(list(map(int, input().split())))
for _ in range(N):
    mat2.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        mat1[i][j] += mat2[i][j]
for k in range(N):
    print(*mat1[k])
