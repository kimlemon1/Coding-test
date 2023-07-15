total = float(input())
Num = int(input())
ans = 0
for i in range(Num):
    M_N = input().split()
    M = int(M_N[0])
    N = int(M_N[1])
    ans += M * N
if total == ans:
    print("Yes")
else:
    print("No")