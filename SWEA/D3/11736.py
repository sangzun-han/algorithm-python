t = int(input())

for tc in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        before = p[i-1]
        mid = p[i]
        after = p[i+1]
        if mid != min(before, mid, after) and mid != max(before, mid, after):
            count += 1
    print("#{} {}".format(tc+1, count))
