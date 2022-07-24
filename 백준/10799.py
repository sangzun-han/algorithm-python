s = input()
stack = []
length = len(s)
ans = 0
for i in range(length):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        if (i - stack[-1] == 1):
            stack.pop()
            ans += len(stack)
        else:
            ans += len(stack)
print(ans)
