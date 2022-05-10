t = int(input())

for tc in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data = [abs(x) for x in data]
    data.sort()
    print("#{} {} {}".format(tc+1, data[0], data.count(data[0])))
