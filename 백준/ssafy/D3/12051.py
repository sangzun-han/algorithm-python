t = int(input())

for tc in range(t):
    n, pd, pg = map(int, input().split())
    check = False
    if pd != 0 and pg == 0:
        print("#{} {}".format(tc+1, "Broken"))
    elif pd != 100 and pg == 100:
        print("#{} {}".format(tc+1, "Broken"))
    else:
        for i in range(1, n+1):
            if i*pd % 100 == 0:
                check = True
                break
        print("#{} {}".format(tc+1, "Possible" if check else "Broken"))
