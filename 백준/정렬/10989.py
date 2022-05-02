import sys

n = int(sys.stdin.readline().strip())
lists = [0] * 10001

for i in range(n):
    lists[int(sys.stdin.readline())] += 1

for i in range(len(lists)):
    if lists[i] != 0:
        for j in range(lists[i]):
            print(i)


'''
메모리 초과
import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
  value = int(sys.stdin.readline().strip())
  data.append(value)
count = [0] * (max(data) + 1)

for i in range(len(data)):
  count[data[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i)
'''
