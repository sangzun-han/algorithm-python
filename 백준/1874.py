import sys

words = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
left = []
right = []
for word in words:
    left.append(word)

for _ in range(n):
    m = list(sys.stdin.readline().split())
    if m[0] == "L":
        if len(left) != 0:
            right.append(left[-1])
            left.pop()

    if m[0] == "D":
        if len(right) != 0:
            left.append(right[-1])
            right.pop()

    if m[0] == "B":
        if len(left) != 0:
            left.pop()

    if m[0] == "P":
        left.append(m[1])

while len(left) != 0:
    right.append(left.pop())

while len(right) != 0:
    print(right.pop(), end='')
