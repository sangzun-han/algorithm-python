from collections import deque

n, k = map(int, input().split())
person = []
queue = deque()
for i in range(1, n+1):
    queue.append(i)

print("<", end='')
for i in range(n-1):
    for j in range(k-1):
        queue.append(queue.popleft())
    print(f"{queue.popleft()},", end=' ')

print(f"{queue.popleft()}", end='')

print(">")
