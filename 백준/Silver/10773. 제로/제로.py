import sys
input = sys.stdin.readline
k = int(input())
ans = []
for _ in range(k):
    val = int(input())
    if val == 0:
        ans.pop(-1)
    else:
        ans.append(val)
print(sum(ans))