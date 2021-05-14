#최대곱 부분수열
import sys

def Maxmul(A):
  Smin = [0 for i in range(len(A))]
  Smax = [0 for i in range(len(A))]
  Smin[0] = A[0]
  Smax[0] = A[0]
  for k in range(1,len(A)):
    Smin[k] = min(Smin[k-1]*A[k], Smax[k-1]*A[k], A[k])
    Smax[k] = max(Smin[k-1]*A[k], Smax[k-1]*A[k], A[k])
  return max(Smin,Smax)
  
n = int(sys.stdin.readline())
A = [0 for i in range(n)]
for i in range(n):
  m = int(sys.stdin.readline())
  A[i] = m 


print(max(Maxmul(A)))
