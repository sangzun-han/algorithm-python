t = int(input())

for i in range(t):
    n = int(input())
    datas = list(map(int, input().split()))

    datas.sort()
    print("#{}".format(i+1), end=' ')
    for data in datas:
        print(data, end=' ')
    print()
