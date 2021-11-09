N = int(input())

if N==1:
    pass

while N!=1:
    for num in range(2,N+1):
      if N % num == 0:
        print(num)
        N = N // num
        break
