t = int(input())

for tc in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    length = len(numbers)
    max_value = float("-inf")
    value = 0
    for i in range(length):
        value += numbers[i]
        max_value = value if max_value < value else max_value
        if value < 0:
            value = 0
    print(f"#{tc+1} {max_value}")
