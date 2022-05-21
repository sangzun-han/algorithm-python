# 1: N극 2: S극
for tc in range(10):
    n = int(input())  # 100으로 고정
    answer = 0
    matrix = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        matrix.append(temp)

    for i in range(n):
        deadlock = False
        for j in range(n):
            if matrix[j][i] == 1:
                deadlock = True
            elif matrix[j][i] == 2:
                if deadlock:
                    answer += 1
                    deadlock = False
    print(f"#{tc+1} {answer}")
