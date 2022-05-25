n, k = map(int, input().split())
temp = list(map(int, input().split()))
max_temp = sum(temp[:k])
result = [max_temp]

for i in range(n-k):
    max_temp = max_temp - temp[i] + temp[i+k]
    result.append(max_temp)

print(max(result))
