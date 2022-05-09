t = int(input())

for tc in range(t):
    n = int(input())
    speed = 0
    dist = 0

    for i in range(n):
        data = list(map(int, input().split()))
        if data[0] == 1:
            speed += data[1]
        elif data[0] == 2:
            speed -= data[1]
            if speed < 0:
                speed = 0
        dist += speed
    print('#{} {}'.format(tc+1, dist))
