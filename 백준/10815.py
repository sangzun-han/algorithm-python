n = int(input())
numbers1 = list(map(int, input().split()))

m = int(input())
numbers2 = list(map(int, input().split()))


for i in range(len(numbers2)):
    if numbers1.count(numbers2[i]) != 0:
        numbers2[i] = 1
    else:
        numbers2[i] = 0

print(*numbers2)
