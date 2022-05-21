matrix = [[0] * 100 for _ in range(100)]
count = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            count += 1
print(count)
