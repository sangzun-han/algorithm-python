t = int(input())
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(t):
    change = int(input())
    result = []

    for money in moneys:
        if change // money == 0:
            result.append(change//money)
        else:
            result.append(change//money)
            change = change - (money) * (change // money)

    print("#{}".format(i+1))
    for result in result:
        print(result, end=' ')
    print()
