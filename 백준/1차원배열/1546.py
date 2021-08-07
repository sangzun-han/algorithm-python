n = int(input())
tList = list(map(int, input().split()))
M = max(tList)

nList = []
for score in tList:
    nList.append(score/M*100)

avg = sum(nList)/n
print(avg)
