t = int(input())

for i in range(t):
    n = int(input())
    sum = 0
    for j in range(1, n+1):
        if j % 2 != 0:
            sum += j
        else:
            sum -= j
    print("#{} {}".format(i+1, sum))
