AB = input()
ls = AB.split()
a = int(ls[0])
b = int(ls[1])
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")