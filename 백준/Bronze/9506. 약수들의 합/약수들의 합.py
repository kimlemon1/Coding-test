val = int(input())

while val != -1:
    start = [1,]
    end = []
    for i in range(2, int(val**(0.5)) + 1):
        if val % i == 0:
            j = val/ i
            if j != i:
                end.insert(0, int(j))
            start.append(i)
    ans = start + end

    if sum(ans) == val:
        print(f"{val} = ", end = "")
        for i in ans:
            if i == 1:
                print(f"{i}", end = "")
            else:
                print(f" + {i}", end = "")
    else:
        print(f"{val} is NOT perfect.", end = "")
    print()
    val = int(input())