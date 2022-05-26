t = int(input())

for tc in range(t):
    answer = 0
    n = int(input())  # 건초 더미 갯수
    data = []
    for i in range(n):
        s = int(input())
        data.append(s)
    avg = sum(data) // n

    for i in range(n):
        answer += abs(data[i] - avg)

    print(f"#{tc+1} {answer//2}")
