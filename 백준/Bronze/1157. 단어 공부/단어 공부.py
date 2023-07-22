in_ = input().upper()
Dict = dict()
for letter in in_:
    try:
        Dict[letter] +=1
    except:
        Dict[letter] = 1
cnt = list(Dict.values())
alp = list(Dict.keys())
max_val = max(cnt)

num = cnt.count(max_val)
if num >1 :
    print("?")
else:
    idx = cnt.index(max_val)
    print(alp[idx])