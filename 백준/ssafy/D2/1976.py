t = int(input())

for i in range(t):
    time = list(map(int, input().split()))
    hh = 0
    mm = time[1] + time[3]
    if mm > 60:
        mm = mm - 60
        hh += 1
    hh += time[0] + time[2]
    if hh > 12:
        hh = hh - 12
    print("#{} {} {}".format(i+1, hh, mm))
