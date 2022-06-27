n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0


def sol(x, y, size):
    global white, blue
    color = matrix[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != matrix[i][j]:
                sol(x, y, size//2)
                sol(x, y+size//2, size//2)
                sol(x+size//2, y, size//2)
                sol(x+size//2, y+size//2, size//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


sol(0, 0, n)
print(white)
print(blue)
