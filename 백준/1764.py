n, m = map(int, input().split())
notHear = set()
notSee = set()

for _ in range(n):
    notHear.add(input())

for _ in range(m):
    notSee.add(input())

notHearSee = notHear.intersection(notSee)
sortList = sorted(notHearSee)
print(len(sortList))
for i in sortList:
    print(i)
