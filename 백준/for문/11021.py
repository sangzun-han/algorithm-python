import sys

a = int(input())

for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
print("Case #{x}: {y}".format(x=i, y=b+c))
