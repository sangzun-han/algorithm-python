N = int(input())
hansu = 0
for i in range(1, N+1):
  if (i<100):
    hansu += 1
  else:
    N = list(map(int, str(i)))
    if N[0]-N[1] == N[1]-N[2]:
      hansu +=1
print(hansu)