# 백준 2667
# 단지번호 붙이기
import sys


def display():
    global cnt, aparts, danji

    print("\n========", cnt, "===============\n")
    for apt in aparts:
        print(apt)

    print(danji)


def dfs(row, column, cnt):
    global N, aparts, danji

    if aparts[row][column] != cnt:
        aparts[row][column] = cnt
        danji[cnt] += 1

    if row > 0 and aparts[row-1][column] == 1:
        aparts[row-1][column] = cnt
        danji[cnt] += 1
        dfs(row-1, column, cnt)

    if row < N-1 and aparts[row+1][column] == 1:
        aparts[row+1][column] = cnt
        danji[cnt] += 1
        dfs(row+1, column, cnt)

    if column > 0 and aparts[row][column-1] == 1:
        aparts[row][column-1] = cnt
        danji[cnt] += 1
        dfs(row, column-1, cnt)

    if column < N-1 and aparts[row][column+1] == 1:
        aparts[row][column+1] = cnt
        danji[cnt] += 1
        dfs(row, column+1, cnt)


N = int(sys.stdin.readline())
aparts = []

for i in range(N):
    apart = sys.stdin.readline().split("\n")[0]
    aparts.append([int(apart[i:i+1]) for i in range(0, len(apart), 1)])

cnt = 2
danji = {}

display()

for row in range(N):
    for column in range(N):
        if aparts[row][column] == 1:
            danji[cnt] = 0
            dfs(row, column, cnt)
            display()
            cnt += 1

values = list(danji.values())
values.sort()

for v in values:
    print(v)
