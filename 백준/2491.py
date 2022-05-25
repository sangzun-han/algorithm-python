n = int(input())
numbers = list(map(int, input().split()))
count = 1
max_count = 1

for i in range(n-1):
    if numbers[i] <= numbers[i+1]:
        count += 1
    else:
        count = 1
    if max_count < count:
        max_count = count

count = 1

for i in range(n-1):
    if numbers[i] >= numbers[i+1]:
        count += 1
    else:
        count = 1
    if max_count < count:
        max_count = count
print(max_count)
