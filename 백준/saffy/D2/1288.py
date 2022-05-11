t = int(input())

for tc in range(t):
    n = int(input())
    count = [0] * 10
    k = 0

    while True:
        if 0 not in count:
            break
        else:
            k += 1
            num = str(n*k)
            for j in range(len(num)):
                count[int(num[j])] += 1
    print("#{} {}".format(tc+1, num))
