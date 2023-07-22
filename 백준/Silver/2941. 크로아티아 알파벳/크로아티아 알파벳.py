string = input()
ans = len(string)
ls = ["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="]
dz = 0
for i, word in enumerate(ls):
    num = string.count(word)
    if i == 2:
        ans -= num * 2
        dz = num
    else:
        ans -= num
    
ans += dz
print(ans)