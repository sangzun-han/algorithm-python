t = int(input())

for tc in range(t):
    n = int(input())
    earn = list(map(int, input().split()))
    avg = sum(earn) / n
    count = 0
    for i in range(n):
        if earn[i] <= avg:
            count += 1
    print("#{} {}".format(tc+1, count))
