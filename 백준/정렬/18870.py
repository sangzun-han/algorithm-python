import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
set_data = sorted(list(set(data)))

dict = {set_data[i]: i for i in range(len(set_data))}

for i in data:
    print(dict[i], end=' ')
