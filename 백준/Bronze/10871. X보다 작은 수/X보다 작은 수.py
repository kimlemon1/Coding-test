N, v = map(int, input().split())
ls = list(map(int, input().split()))
for i in range(N):
    if ls[i] < v:
        print(ls[i], sep = "")