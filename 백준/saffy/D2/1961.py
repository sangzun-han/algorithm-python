t = int(input())


def rotate(matrix, N):
    new_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_matrix[i][j] = matrix[N-1-j][i]

    return new_matrix


for i in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    rotate90 = rotate(matrix, n)
    rotate180 = rotate(rotate90, n)
    rotate270 = rotate(rotate180, n)
    print("#{}".format(i+1))

    for i in range(n):
        print("".join(map(str, rotate90[i])), end=" ")
        print("".join(map(str, rotate180[i])), end=" ")
        print("".join(map(str, rotate270[i])), end=" ")
        print()
