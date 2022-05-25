n = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, n+1, number):
            switch[i] = 0 if switch[i] else 1

    elif gender == 2:
        if number + 1 > n or number - 1 < 1:
            switch[number] = 0 if switch[number] else 1
        else:
            if switch[number-1] == switch[number+1]:
                left = number - 1
                right = number + 1

                while True:
                    if left - 1 < 1 or right + 1 > n:
                        break
                    if switch[left - 1] != switch[right + 1]:
                        break
                    else:
                        left -= 1
                        right += 1

                for i in range(left, right+1):
                    switch[i] = 0 if switch[i] else 1
            else:
                switch[number] = 0 if switch[number] else 1


for i in range(1, n, 20):
    print(*switch[i:i+20])
