t = int(input())

for tc in range(t):
    n = int(input())

    avg = 0
    for i in range(n):
        p, x = map(float, input().split())
        avg += p*x
    print("#{} {}".format(tc+1, round(avg, 6)))
