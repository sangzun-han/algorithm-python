a, p = map(int, input().split())
data = [a]

# 자리수 분리
while True:
    index = 0
    number = list(map(int, str(a)))
    sum = 0
    for num in number:
        sum += num**p
        index += 1

    if sum in data:
        index2 = data.index(sum)
        data = data[:index2]
        break
    else:
        data.append(sum)
        a = sum

print(len(data))
