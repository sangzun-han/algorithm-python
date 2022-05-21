t = int(input())

for tc in range(t):
    d, l, n = map(int, input().split())
    damage = d
    for i in range(1, n):
        damage += d*(1+i*l/100)
    print("#{} {}".format(tc+1, round(damage)))
