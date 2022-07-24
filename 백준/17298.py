n = int(input())
numbers = list(map(int, input().split()))
ans = [-1] * n
stack = []

stack.append(0)

for i in range(1, n):
    while stack and numbers[stack[-1]] < numbers[i]:
        ans[stack.pop()] = numbers[i]
    stack.append(i)
print(*ans)
