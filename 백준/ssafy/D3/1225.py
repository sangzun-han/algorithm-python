for _ in range(10):
    t = input()
    data = list(map(int, input().split()))

    while min(data) != 0:
        for i in range(5):
            temp = data[0] - (i+1)
            temp = 0 if temp <= 0 else temp
            data.append(temp)
            del data[0]
            if temp == 0:
                break

    print(f"#{t}", end=' ')
    for data in data:
        print(data, end=' ')
    print()
