N = int(input())
index = 0
sum = 0

# N은 몇번째 행 ?
while(True):
  index+=1
  sum = int(index * (index+1) / 2) # 등차수열 합 n(n+1)/2
  if (N <= sum):
    break

# 행에서 몇번째 값 ? 
num = int(N-(index -1)*index/2) # 주어진 N에서 구한 index전까지의 합 뺀다 (등차수열 합)

# 역방향 or 순방향
if (index%2==0):
  print('{0}/{1}'.format(num,index-num+1))
else:
    print('{0}/{1}'.format(index-num+1,num))

 
 
