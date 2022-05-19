def dfs(count):
    global answer

    if count == 0:
        temp = int(''.join(values))

        if answer < temp:
            answer = temp
        return
    for i in range(length):
        for j in range(i+1, length):
            values[i], values[j] = values[j], values[i]
            temp_key = ''.join(values)

            if visited.get((temp_key, count-1), 1):
                visited[(temp_key, count-1)] = 0
                dfs(count - 1)
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    # 바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    # 계속 쓸꺼니까 캐스팅
    length = len(values)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t+1, answer))
