matrix = [[0] * 1001 for _ in range(1001)]

n = int(input())

for i in range(n):
    x, y, width, height = map(int, input().split())
    for j in range(y, y+height):
        matrix[j][x:x+width] = [i+1]*width

for i in range(n):
    answer = 0
    for j in range(len(matrix)):
        answer += matrix[j].count(i+1)
    print(answer)
