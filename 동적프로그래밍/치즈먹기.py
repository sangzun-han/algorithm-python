# N * N개의 칸이 있는 테이블이 있고, 치즈 몇 개가 테이블에 놓여있다. 치즈를 좋아하
# 는 생쥐 미키는 테이블의 (1,1)에서 출발해서 (N,N)에 도착할 때까지 많은 치즈를 먹고
# 싶어한다. 하지만 머리가 나쁜 미키는 위로 올라가거나 오른쪽으로만 이동할 수 있다. 

# 입력은 표준입력(standard input; 키보드를 통한 입력)을 사용한다. 입력은 첫 줄에 자
# 연수 N과 M이 주어진다. 이 때, N과 M은 1 이상 10000 이하의 범위이다. 다음 M개의
# 줄에 각각의 치즈의 위치 x와 y가 주어진다.

import sys

n,m= map(int,sys.stdin.readline().split())
cheese = [[0] * n for i in range(n)]

def Maxway(i,j):
  if(cheese[i-1][j] > cheese[i][j-1]):
    return cheese[i-1][j]
  else:
    return cheese[i][j-1]

def Eatcheese(n):
  for i in range(m):
      x,y= map(int,sys.stdin.readline().split())
      cheese[x-1][y-1] = 1
  
  if (len(cheese)==1):
    return 1
  elif (len(cheese)==1 and m==0):
    return 0
  
  for i in range(1,n):
    print("\n")
    for j in range(1,n):
      print(cheese[i][j], end=" ") # 배열 확인

  print("\n")
  for i in range(1,n):
    print("\n")
    for j in range(1,n):
      cheese[i][j] = cheese[i][j] + Maxway(i,j)
  return cheese[i][j]

print(Eatcheese(n))
