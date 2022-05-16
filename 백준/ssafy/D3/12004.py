t = int(input())

for tc in range(t):
    n = int(input())
    check = False
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j == n:
                check = True
                break
    print("#{} {}".format(tc+1, "Yes" if check else "No"))
