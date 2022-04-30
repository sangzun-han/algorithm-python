import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

# 정렬
arr.sort()

# 평균
print(round(sum(arr) / n))

# 중앙값
print(arr[n//2])

# 최빈값
count = Counter(arr).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

# 범위
print(abs(arr[-1] - arr[0]))
