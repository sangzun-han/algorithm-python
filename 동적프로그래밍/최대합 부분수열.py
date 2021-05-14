#최대합 부분수열
# A = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
import sys

def Maxsum(A):
  start,end = 0,0
  S = [0 for i in range(len(A))]
  S[0] = A[0]
  for k in range(1,len(A)):
    S[k] = max(S[k-1]+A[k], A[k])
    if (S[k-1]+A[k] > A[k]):
      start = k
    else:
      start = k
      end = k
  print(end,start,end=" ")
  return max(S)


n = int(sys.stdin.readline())
A = [0 for i in range(n)]
lst = A = [0 for i in range(n)]
for i in range(n):
  m = int(sys.stdin.readline())
  A[i] = m 


print(Maxsum(A))
