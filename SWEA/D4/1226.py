n = 16
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(10):
    ans = 0
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                x, y = i, j
    stack = [(x, y)]

    while stack:
        nx, ny = stack.pop()
        for i in range(4):
            ex = nx + dx[i]
            ey = ny + dy[i]
            if 0 < ex < n and 0 < ey < n:
                if matrix[ex][ey] == 0:
                    stack.append((ex, ey))
                    matrix[ex][ey] = 5
                elif matrix[ex][ey] == 3:
                    ans = 1
                    stack.clear()
                    break
    print(f"#{tc} {ans}")
