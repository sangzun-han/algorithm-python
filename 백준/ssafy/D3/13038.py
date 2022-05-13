t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_value = float('inf')
    for i in range(len(a)):
        if a[i] == 0:
            continue
        start = i
        count = 0
        answer = 0
        while True:
            if a[start % 7] == 1:
                count += 1
            start += 1
            answer += 1
            if count == n:
                min_value = min(min_value, answer)
                break

    print("#{} {}".format(tc+1, min_value))
