'''
시간 초과
import sys

n  = int(input())
arr = []
temp = 0

for i in range(n):
  x,y = map(int, sys.stdin.readline().split())
  arr.append([x,y])

for i in range(n):
  for j in range(i+1,n):
    if arr[i][1] > arr[j][1]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    elif arr[i][1] == arr[j][1]:
      if arr[i][0] > arr[j][0]:
        temp = arr[i]
        arr[i] = temp
        arr[j] = temp

for i in range(n):
  print(arr[i][0], arr[i][1])
'''


import sys

n = int(input())
arr = []
temp = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])
