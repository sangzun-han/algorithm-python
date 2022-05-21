t = int(input())

for tc in range(t):
    p, q = map(float, input().split())

    s1 = (1-p) * q
    s2 = p*(1-q)*q

    if s1 < s2:
        print("#{} {}".format(tc+1, "YES"))
    else:
        print("#{} {}".format(tc+1, "NO"))
