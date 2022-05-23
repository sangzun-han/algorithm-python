# 가장 큰 높이 찾기 (L값,H값)
# 가장 큰 높이 기준으로 왼쪽 -> 가장 큰 높이까지 높이 계속 더해주기
# 가장 큰 높이 기준으로 오른쪽 -> 끝에서 가장 큰높이까지 높이 계속 더해주기
data = []
n = int(input())
maxL, maxH = 0, 0
for _ in range(n):
    L, H = map(int, input().split())
    data.append((L, H))

    if maxL < L:
        maxL = L
    if maxH < H:
        maxH = H
        index = L

matrix = [0] * (maxL+1)
for l, h in data:
    matrix[l] = h

temp = 0
answer = 0
for i in range(index):
    if matrix[i] > temp:
        temp = matrix[i]
    answer += temp
answer += maxH

temp = 0
for i in range(maxL, index, -1):
    if matrix[i] > temp:
        temp = matrix[i]
    answer += temp

print(answer)
