t = int(input())

for tc in range(t):
    n, d = map(int, input().split())
    range = d * 2 + 1
    if n % range == 0:
        answer = int(n/range)
    else:
        answer = int(n/range+1)
    print("#{} {}".format(tc+1, answer))
