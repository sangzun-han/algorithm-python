def dfs():

    # stack의 길이가 M이 되면 출력
    if len(stack) == M:
        print(' '. join(list(map(str, stack))))
    else:
        for num in range(1, N+1):
            if num not in stack:
                stack.append(num)
                dfs()
                stack.pop()


N, M = map(int, input().split())
stack = []
dfs()
