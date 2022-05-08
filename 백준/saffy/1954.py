t = int(input())
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

for tc in range(t):
    n = int(input())
    x, y = 0, 0
    mode = 0
    matrix = [[0] * n for _ in range(n)]

    for i in range(1, n*n+1):
        matrix[x][y] = i
        x += row[mode]
        y += col[mode]

        if x < 0 or y < 0 or x >= n or y >= n or matrix[x][y] != 0:
            x -= row[mode]
            y -= col[mode]

            mode = (mode + 1) % 4

            x += row[mode]
            y += col[mode]

    print("#{}".format(tc+1))

    for j in range(len(matrix)):
        for k in range(len(matrix)):
            print(matrix[j][k], end=' ')
        print()
