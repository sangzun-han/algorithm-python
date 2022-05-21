t = int(input())

for tc in range(t):
    p = input().strip()
    q = input().strip()

    if p + "a" != q:
        print("#{} {}".format(tc+1, "Y"))
    else:
        print("#{} {}".format(tc+1, "N"))
