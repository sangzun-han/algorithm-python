N = int(input())

def prime(n):
  if n<2:
    return -1
  
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return -1
  
  return 1

for i in range(N):
  M = int(input())

  a= int(M/2) 
  b= int(M/2)

  for j in range(int(M/2)):
    if prime(a)==1 and prime(b)==1:
      print(a,b)
      break
    else:
      a-=1
      b+=1

