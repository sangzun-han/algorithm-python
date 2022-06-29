import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}

for i in range(1, n+1):
    pocketmon = sys.stdin.readline().strip()
    dict[i] = pocketmon
    dict[pocketmon] = i

for i in range(m):
    ans = sys.stdin.readline().strip()
    if ans.isdigit():
        print(dict[int(ans)])
    else:
        print(dict[ans])
