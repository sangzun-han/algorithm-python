t = int(input())

for tc in range(t):
    n = int(input())
    routes = []
    result = []
    count = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        routes.append((a, b))

    for a, b in routes:
        for i in range(a, b+1):
            count[i] += 1

    p = int(input())

    for i in range(p):
        c = int(input())
        result.append(count[c])

    print("#{}".format(tc+1), end=' ')
    for result in result:
        print(result, end=' ')
    print()
