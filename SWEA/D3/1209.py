for _ in range(10):
    t = int(input())
    max_sum = 0
    diag = 0
    matrix = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if sum(matrix[i]) > max_sum:
            max_sum = sum(matrix[i])

    new_arr = list(zip(*matrix))
    for i in range(100):
        if sum(new_arr[i]) > max_sum:
            max_sum = sum(new_arr[i])

    for i in range(100):
        diag += matrix[i][i]
    if max_sum < diag:
        max_sum = diag

    diag = 0
    for i in range(100):
        diag += matrix[99-i][i]
    if max_sum < diag:
        max_sum = diag

    print(f"#{t} {max_sum}")
