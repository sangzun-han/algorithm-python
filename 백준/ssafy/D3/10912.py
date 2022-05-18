t = int(input())

for tc in range(t):
    n = list(input())
    m = []
    for i in n:
        if n.count(i) >= 2:
            m.append(i)

    for i in m:
        if n.count(i) % 2 == 1:
            while n.count(i) != 1:
                n.remove(i)
        else:
            while n.count(i) != 0:
                n.remove(i)

    n.sort()

    if len(n) == 0:
        print("#{} {}".format(tc+1, "Good"))
    else:
        print("#{}".format(tc+1), end=' ')
        for i in n:
            print(i, end='')
        print()
