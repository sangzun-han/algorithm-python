import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    order = cmd[0]
    if order == "push":
        value = cmd[1]
        stack.append(value)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
