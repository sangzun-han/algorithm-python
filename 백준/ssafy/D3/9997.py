t = int(input())

for tc in range(t):
    n = int(input())
    rad = 2*n
    time = 0
    minute = 0
    if rad == 0:
        print("#{} {} {}".format(tc+1, 0, 0))
    else:
        time = rad // 60
        minute = rad - (time*60)
        print("#{} {} {}".format(tc+1, time, minute))
