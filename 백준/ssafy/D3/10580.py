t = int(input())

for tc in range(t):
    n = int(input())
    pipes = []
    count = 0
    for _ in range(n):
        temp = list(map(int, input().split()))
        pipes.append(temp)

    for i in range(n):
        for j in range(i+1, n):
            if pipes[i][0] > pipes[j][0] and pipes[i][1] < pipes[j][1]:
                count += 1
            if pipes[i][0] < pipes[j][0] and pipes[i][1] > pipes[j][1]:
                count += 1
    print("#{} {}".format(tc+1, count))
