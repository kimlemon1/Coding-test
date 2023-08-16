import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = input()
    stack = 0
    false_flag = True
    for i in range(len(string)):
        if string[i] == "(":
            stack += 1
        elif string[i] == ")":
            stack -= 1
        if stack < 0:
            false_flag = False
            break
    if false_flag == False or stack != 0:
        print("NO")
    else:
        print("YES")