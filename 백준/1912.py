n = int(input())
numbers = list(map(int, input().split()))
value = 0
max_value = float("-inf")

for i in range(n):
    value += numbers[i]
    max_value = value if max_value < value else max_value
    if value < 0:
        value = 0

print(max_value)
