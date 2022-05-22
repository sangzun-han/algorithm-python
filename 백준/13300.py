n, k = map(int, input().split())
man_grade = [0, 0, 0, 0, 0, 0, 0]
woman_grade = [0, 0, 0, 0, 0, 0]
count = 0
for _ in range(n):
    s, y = map(int, input().split())

    if s == 0:
        woman_grade[y-1] += 1
    elif s == 1:
        man_grade[y-1] += 1

for i in range(len(man_grade)):
    if man_grade[i] == 0:
        count = count
    elif man_grade[i] <= k:
        count += 1
    else:
        if man_grade[i] % k == 0:
            count += man_grade[i] // k
        else:
            count += (man_grade[i] // k) + 1

for i in range(len(woman_grade)):
    if woman_grade[i] == 0:
        count = count
    elif woman_grade[i] <= k:
        count += 1
    else:
        if woman_grade[i] % k == 0:
            count += woman_grade[i] // k
        else:
            count += (woman_grade[i] // k) + 1
print(count)
