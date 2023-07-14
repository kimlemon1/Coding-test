ABC = input()
ls = ABC.split()
ans = 0
for i in range(len(ls)):
    ans += int(ls[i])
print(ans)