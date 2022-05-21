t = int(input())

for tc in range(t):
    n = int(input())
    pos = []
    indexes = [0] * 101
    grades = list(map(int, input().split()))
    for i in range(0, len(grades)):
        indexes[grades[i]] = indexes[grades[i]] + 1

    for i in range(len(indexes)):
        if indexes[i] == max(indexes):
            pos.append(i)

    print("#{} {}".format(n, pos[-1]))
