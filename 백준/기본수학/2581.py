import time
start = time.time()

M = int(input())
N = int(input())

lists = []

for num in range(M,N+1):
    error=0
    if num > 1:
      for i in range(2,num):
        if num % i == 0:
          error +=1
          break
      if error==0:
        lists.append(num)

if len(lists) > 0:
    print(sum(lists))
    print(min(lists))
else:
    print(-1)
  
print("time : ", time.time() - start)