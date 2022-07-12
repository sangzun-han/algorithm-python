from collections import deque


t = int(input())
move = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0<=nx<n and 0<=ny<n:
                if ans[x][y] + matrix[nx][ny] < ans[nx][ny]:
                    ans[nx][ny] = matrix[nx][ny] + ans[x][y]
                    queue.append((nx,ny))

for tc in range(t):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    ans = [[1000] * n for _ in range(n)]
    ans[0][0] = matrix[0][0]
    bfs(0,0)
    print(f"#{tc+1} {ans[n-1][n-1]}")
    