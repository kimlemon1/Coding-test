H_M = input().split()
H = int(H_M[0])
M = int(H_M[1])

dur = int(input())
M += dur
while (M >= 60):
    H = H + 1
    M -= 60
    if H == 24:
        H = 0
print(f"{H} {M}")