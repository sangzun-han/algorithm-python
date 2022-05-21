t = int(input())

for tc in range(t):
    a, b = map(int, input().split())

    if a >= 10 or b >= 10:
        print("#{} {}".format(tc+1, -1))
    else:
        print("#{} {}".format(tc+1, a*b))
