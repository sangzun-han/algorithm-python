t = int(input())

for i in range(t):
    sum = 0
    datas = list(map(int, input().split()))
    datas.remove(max(datas))
    datas.remove(min(datas))

    for data in datas:
        sum += data
    print("#{} {}".format(i+1, round(sum/len(datas))))
