t = int(input())
datas = [2, 3, 5, 7, 11]
for tc in range(t):
    n = int(input())
    count = [0] * 5
    for i in range(5):
        while True:
            if n % datas[i] == 0:
                count[i] += 1
                n = n // datas[i]
            else:
                break
    print("#{}".format(tc+1), end=' ')
    for cnt in count:
        print(cnt, end=' ')
    print()
