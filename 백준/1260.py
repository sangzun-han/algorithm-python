n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
graph2 = [[0] * (n+1) for _ in range(n+1)]

dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    graph2[x][y] = graph[y][x] = 1


def dfs(v):
    dfs_visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if dfs_visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    bfs_visited[v] = 1

    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if bfs_visited[i] == 0 and graph2[v][i] == 1:
                queue.append(i)
                bfs_visited[i] = 1


dfs(v)
bfs(v)
