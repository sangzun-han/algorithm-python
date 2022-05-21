t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    max_value = 0
    if a < b:
        for j in range(b-a+1):
            sum = 0
            for k in range(a):
                sum += Ai[k] * Bj[j+k]
            max_value = max(max_value, sum)
    elif a > b:
        for j in range(a-b+1):
            sum = 0
            for k in range(b):
                sum += Ai[j+k] * Bj[k]
            max_value = max(max_value, sum)
    else:
        sum = 0
        for j in range(a):
            sum += Ai[j] * Bj[j]
        max(max_value, sum)

    print("#{} {}".format(i+1, max_value))
