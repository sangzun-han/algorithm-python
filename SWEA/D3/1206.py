for tc in range(10):
    n = int(input())
    building = list(map(int, input().split()))

    count = 0
    for i in range(2, n-2):
        around = max(building[i-2], building[i-1],
                     building[i+1], building[i+2])
        if building[i] > around:
            count += building[i] - around

    print(f"#{tc+1} {count}")
