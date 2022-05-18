t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    if n % m == 0:
        print("#{} {}".format(tc+1, "0"))
    else:
        print("#{} {}".format(tc+1, "1"))
