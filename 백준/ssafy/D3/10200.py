t = int(input())

for tc in range(t):
    n, a, b = map(int, input().split())
    max_value = a if a <= b else b
    if a+b > n:
        min_value = a+b-n
    elif a+b <= n:
        min_value = 0
    print("#{} {} {}".format(tc+1, max_value, min_value))
