t = int(input())

for i in range(t):
    data = list(map(int, input().split()))
    print("#{} {}".format(i+1, max(data)))
