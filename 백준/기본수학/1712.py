import sys

A,B,C = map(int, sys.stdin.readline().split())
if C-B == 0:
  sys.exit(1)
if B>C:
  print(-1)
elif A/(C-B):
  print(int(A/(C-B)+1))