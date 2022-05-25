height = []

for _ in range(9):
    n = int(input())
    height.append(n)

total = sum(height)

for i in range(9):
    for j in range(i+1, 9):
        if total - (height[i] + height[j]) == 100:
            num1, num2 = height[i], height[j]
            height.remove(num1)
            height.remove(num2)
            height.sort()

            for i in height:
                print(i)
            break

    if len(height) < 9:
        break
