N = int(input())

cnt = 1
nums = 1
while N > nums:
  nums = (cnt*6)+nums
  cnt +=1
print(cnt)