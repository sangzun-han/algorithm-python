N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
      for j in range(i+i, N, i):
        sieve[j] = False

while True:
    M = int(input())
    if M==0:
      break
    cnt = 0
  
    for i in range(M+1, M*2+1):
      if i>1 and sieve[i]:
        cnt +=1
    print(cnt)