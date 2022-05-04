t = int(input())
for i in range(t):
    max_value = 0
    table = []
    n, m = map(int, input().split())

    for j in range(n):
        data = list(map(int, input().split()))
        table.append(data)

    for k in range(n-m+1):
        for l in range(n-m+1):
            value = 0
            for q in range(k, k+m):
                for r in range(l, l+m):
                    value += table[q][r]
            max_value = max(max_value, value)
    print("#{}".format(i+1), end=' ')
    print(max_value)
