ABC = input().split()

a = int(ABC[0])
b = int(ABC[1])
c = int(ABC[2])

if a==b == c:
    print(10000 + a * 1000)
elif a != b and a != c and b != c:
    print(max(a,b,c) * 100)
else:
    if a == b or a == c:
        val = a
    else:
        val = b
    print(1000 + val * 100)