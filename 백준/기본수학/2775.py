import sys

T = int(input())

for i in range(T):
  K = int(input())
  N = int(input())
  
  floor = [x for x in range(1,N+1)]

  for x in range(K):
    for y in range(1,N):
      floor[y] = floor[y] + floor[y-1]
  print(floor[-1])
