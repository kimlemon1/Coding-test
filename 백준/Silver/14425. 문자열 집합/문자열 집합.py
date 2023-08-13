import sys
input = sys.stdin.readline
n, m = map(int, input().split())
set_s = set()
for _ in range(n):
    set_s.add(input())
search_list = list()
for _ in range(m):
    search_list.append(input())

count = 0
for str in search_list:
    if str in set_s:
        count += 1
print(count)