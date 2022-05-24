c, r = map(int, input().split())
k = int(input())
matrix = [[0] * c for _ in range(r)]

if k > c*r:
    print(0)
    exit()
# 우상좌하
row = [1, 0, -1, 0]
col = [0, 1, 0, -1]
x, y, mode = 0, 0, 0

for i in range(1, c*r+2):

    if i == k:
        print(y+1, x+1)
        # exit()
    else:
        matrix[x][y] = i
        x += row[mode]
        y += col[mode]

        if x < 0 or y < 0 or x >= r or y >= c or matrix[x][y] != 0:
            x -= row[mode]
            y -= col[mode]

            mode = (mode + 1) % 4

            x += row[mode]
            y += col[mode]
