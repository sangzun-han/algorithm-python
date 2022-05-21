radius = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
value = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t = int(input())

for tc in range(t):
    n = int(input())
    answer = 0
    for i in range(n):
        x, y = map(int, input().split())
        distance = (x*x + y*y)**0.5

        for rad, p in zip(radius, value):
            if distance <= rad:
                answer += p
                break
    print("#{} {}".format(tc+1, answer))
