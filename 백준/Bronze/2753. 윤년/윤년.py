year = int(input())
if year % 4:
    ans = 0
else:
    if year % 100:
        ans =1
    else:
        if not year % 400:
            ans = 1
        else :
            ans = 0
print(ans)