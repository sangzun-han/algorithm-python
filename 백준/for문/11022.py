import sys

a = int(input())

for i in range(1, a+1):
    b, c = map(int, sys.stdin.readline().split())
    print("Case #{x}: {y} + {z} = {v}".format(x=i, y=b, z=c, v=b+c))
