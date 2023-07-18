ls = []
for j in range(9):
    ls.append(int(input()))

max_idx = 0
max_val = ls[0]

for i in range(1, len(ls)):
    if max_val < ls[i]:
        max_val = ls[i]
        max_idx = i
        
print(max_val)
print(max_idx+1)