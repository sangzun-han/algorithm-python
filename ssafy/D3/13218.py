t = int(input())

for tc in range(t):
    n = int(input())

    if n < 3:
        print("#{} {}".format(tc+1, 0))
    else:
        print("#{} {}".format(tc+1, n//3))
