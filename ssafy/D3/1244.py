def dfs(change):
    global answer

    if change == 0:
        temp = int(''.join(money))

        if answer < temp:
            answer = temp
        return answer

    for i in range(length):
        for j in range(i+1, length):
            money[i], money[j] = money[j], money[i]
            money_key = ''.join(money)

            if visited.get((money_key, change-1), 1):
                visited[(money_key, change-1)] = 0
                dfs(change-1)
            else:
                money[i], money[j] = money[j], money[i]


t = int(input())

for tc in range(t):
    answer = -1
    money, change = input().split()
    money = list(money)
    change = int(change)
    length = len(money)
    visited = {}
    dfs(change)
    print(f'# {tc+1} {answer}')
