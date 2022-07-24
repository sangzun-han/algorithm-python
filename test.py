n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]
ans = 0
cnt = 0
maxi = 0

for i in range(n):
    for j in range(n):
        ans = 0
        row = i
        col = j
        for d in range(8):
            cnt = 0
            for k in range(n):
                col += dc[d]
                row += dr[d]
                if(row < n and row >= 0 and col < n and col >= 0):
                    if matrix[row][col] == 0:
                        if cnt <= 1:
                            cnt = 0
                            ans += 1
                    elif matrix[row][col] == 1:
                        cnt += 1
                        if (cnt > 1):
                            cnt = 0
                            break
                else:
                    break
        maxi = max(ans, maxi)

print(maxi)
