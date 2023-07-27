N, M = map(int, input().split())
ls = list(map(int, input().split()))

max = 0
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        for k in range(j +1, len(ls)):
            if (max < ls[i] + ls[j] + ls[k]) and (M >= ls[i] + ls[j] + ls[k]):
                max = ls[i] + ls[j] + ls[k]
print(max)