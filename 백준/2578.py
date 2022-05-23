matrix = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
numbers = []
num = 0


def check_bingo(matrix):
    bingo = 0
    col = 0
    row = 0

    for i in range(5):
        row = 0
        for j in range(5):
            row += matrix[i][j]
        if row == 0:
            bingo += 1

    for i in range(5):  # 세로
        col = 0
        for j in range(5):
            col += matrix[j][i]
        if col == 0:
            bingo += 1

    if matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0 and matrix[3][3] == 0 and matrix[4][4] == 0:
        bingo += 1
    if matrix[4][0] == 0 and matrix[3][1] == 0 and matrix[2][2] == 0 and matrix[1][3] == 0 and matrix[0][4] == 0:
        bingo += 1
    return bingo


for i in range(5):
    for j in range(5):
        numbers.append(mc[i][j])


for number in numbers:
    for i in range(5):
        for j in range(5):
            if number == matrix[i][j]:
                matrix[i][j] = 0
                num += 1
                answer = check_bingo(matrix)
                if answer >= 3:
                    print(num)
                    exit()
