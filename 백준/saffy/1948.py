month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


t = int(input())

for tc in range(t):
    result = 0
    m1, d1, m2, d2 = map(int, input().split())
    for j in range(m1, m2):
        if m1 == j:
            result += month[j] - d1 + 1
        else:
            result += month[j]
    result += d2
    print("#{} {}".format(tc+1, result))
