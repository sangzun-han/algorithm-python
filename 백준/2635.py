n = int(input())
length = 0
answer = []
for i in range(n//2, n+1):
    data = [n, i]
    idx = 0
    while True:
        last_num = data[idx] - data[idx+1]
        if last_num >= 0:
            data.append(last_num)
            idx += 1
            if length < len(data):
                length = len(data)
                answer = data[:]
        else:
            break

print(len(answer))
for ans in answer:
    print(ans, end=' ')
