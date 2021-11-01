import sys

T = int(input())
for i in range(T):
  H,W,N = map(int, sys.stdin.readline().split())
  floor = 0
  hosu = 0
  if N % H == 0:
    floor = H*100
    hosu =  N // H
  else:
    floor = (N % H) * 100
    hosu = 1 + N // H
  print(floor+hosu)

