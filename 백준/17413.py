s = input()
s += " "
tag = False
stack = []
for s in s:
    if s == "<":
        while stack:
            print(stack.pop(), end='')
        print(s, end='')
        tag = True
    elif s == ">":
        tag = False
        print(s, end='')
    elif (tag):
        print(s, end='')
    else:
        if s == " ":
            while stack:
                print(stack.pop(), end='')
            print("", end=' ')
        else:
            stack.append(s)
