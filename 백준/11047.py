n, k = map(int, input().split())
datas = []
ans = 0
for _ in range(n):
    datas.append(int(input()))

length = len(datas) - 1


while True:
    if k < datas[length]:
        length -= 1
    elif k >= datas[length]:
        count = k//datas[length]
        k -= datas[length] * count
        ans += count
        if k <= 0:
            break
        length -= 1

print(ans)
