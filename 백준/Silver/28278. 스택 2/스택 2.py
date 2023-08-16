import sys
class Stack():
    def __init__(self):
        self.s_ls = []
        
    def add(self, x):
        self.s_ls.append(x)
        
    def pop(self):
        if len(self.s_ls) ==0: # list는 비어있는거 판단 불가. queue만 된다
            print(-1)
        else:
            print(self.s_ls.pop(-1))
    def lenght(self):
        print(len(self.s_ls))
    def is_empty(self):
        if len(self.s_ls):
            print(0)
        else:
            print(1)
    
    def get(self):
        if len(self.s_ls) ==0: # list는 비어있는거 판단 불가. queue만 된다
            print(-1)
        else:
            print(self.s_ls[-1]) 

stack = Stack()
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = input()
    if line[0] == '1':
        func, val = map(int, line.split())
        stack.add(val)
    else:
        func = int(line[0])
        
        if func == 2:
            stack.pop()
        elif func == 3:
            stack.lenght()
        elif func == 4:
            stack.is_empty()
        elif func == 5:
            stack.get()