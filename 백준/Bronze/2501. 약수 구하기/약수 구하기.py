N, K = map(int, input().split())
start = []
end = []
for i in range(1, int(N**(0.5)) + 1):
    if N % i == 0:
        j = N / i
        if j != i:
            end.insert(0, int(j))
        start.append(i)
ans = start + end
if K > len(ans):
    print(0)
else:
    print(ans[K-1])