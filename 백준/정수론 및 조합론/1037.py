import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
max_value = max(data)
min_value = min(data)

print(max_value * min_value)
