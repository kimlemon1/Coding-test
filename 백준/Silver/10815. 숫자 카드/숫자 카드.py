import sys
#input = sys.stdin.readline
n = int(input())

ls_card= set(map(int, input().split()))

m = int(input())

ls_search= list(map(int, input().split()))

def search(ls_card, val):
    return int(val in ls_card)

ans = []
for v in ls_search:
    ans.append(search(ls_card, v))
for j in ans:
    print(j, end=' ')