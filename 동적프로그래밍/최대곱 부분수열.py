#최대곱 부분수열
import sys
# A = [2,3,-3,4,5]
# A = [3,-2,1,0,-8,-9]
# A = [-6,12,-7,0,14,-7,5]
# A = [5,1,-3,-8]
# A = [1,1,-11,-2,-3,5,0,0]
X = [0 for i in range(len(A))]
def Maxmul(A):
  Smin = [0 for i in range(len(A))]
  Smax = [0 for i in range(len(A))]
  Smin[0] = A[0]
  Smax[0] = A[0]
  start,end = 0,0
  for k in range(1,len(A)):
    Smin[k] = min(Smin[k-1]*A[k], Smax[k-1]*A[k], A[k])
    Smax[k] = max(Smin[k-1]*A[k], Smax[k-1]*A[k], A[k])
  if (max(Smax) < max(Smin)):
    end = Smin.index(max(Smin))
  else:
    end = Smax.index(max(Smax))
  
  for k in range(len(A)-1,0,-1):
    X[k-1] = X[k] *A[k-1]
    if (X[k] == max(Smax)):
      start = k 
  print(start,end)
  return max(Smin,Smax)
  
n = int(sys.stdin.readline())
A = [0 for i in range(n)]
for i in range(n):
  m = int(sys.stdin.readline())
  A[i] = m 
print(max(Maxmul(A)))
