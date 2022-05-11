t = int(input())

for tc in range(t):
    count = 0
    datas = list(map(str, input()))

    if 15 - len(datas) >= 8:
        print("#{} {}".format(tc+1, "YES"))
    else:
        for data in datas:
            if data == 'o':
                count += 1
        temp_vic = 8 - count
        if temp_vic <= 15 - len(datas):
            print("#{} {}".format(tc+1, "YES"))
        else:
            print("#{} {}".format(tc+1, "NO"))
