t = int(input())

for tc in range(t):
    n = int(input())
    check = True
    matrix = []
    coordinates = [[] for _ in range(n)]

    for i in range(n):
        matrix.append(list(input()))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                coordinates[i].append(j)

    res = []

    for i in coordinates:
        if len(i) > 0:
            res.append(i)
    ans = res[0]

    if len(ans) != len(res):
        check = False
    else:
        for i in range(1, len(res)):
            if res[i] != res[i-1]:
                check = False
                break
        for i in range(1, len(ans)):
            if ans[i] != ans[i-1] + 1:
                check = False
                break
    print("#{}".format(tc+1), end=' ')
    print("yes" if check else "no")
