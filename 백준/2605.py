student = int(input())
numbers = list(map(int, input().split()))
answer = []

for i in range(student):
    answer.insert(i-numbers[i], i+1)

for ans in answer:
    print(ans, end=' ')
