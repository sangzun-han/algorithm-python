a, b = map(int, input().split())
c = int(input())

if b+c < 60:
    print(f"{a} {b+c}")
else:
    temp = (b+c) // 60
    a += temp
    if a >= 24:
        a = a - 24
    print(f"{a} {(b+c)%60}")
