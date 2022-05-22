n = int(input())
answer = []
for _ in range(n):
    a_star = 0
    b_star = 0

    a_circle = 0
    b_circle = 0

    a_square = 0
    b_square = 0

    a_triangle = 0
    b_triangle = 0

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_count = a[0]
    b_count = b[0]
    del a[0], b[0]

    for i in range(len(a)):
        if a[i] == 4:
            a_star += 1
        elif a[i] == 3:
            a_circle += 1
        elif a[i] == 2:
            a_square += 1
        elif a[i] == 1:
            a_triangle += 1

    for i in range(len(b)):
        if b[i] == 4:
            b_star += 1
        elif b[i] == 3:
            b_circle += 1
        elif b[i] == 2:
            b_square += 1
        elif b[i] == 1:
            b_triangle += 1

    if a_star > b_star:
        answer.append("A")
    elif a_star < b_star:
        answer.append("B")
    elif a_star == b_star and a_circle > b_circle:
        answer.append("A")
    elif a_star == b_star and a_circle < b_circle:
        answer.append("B")
    elif a_star == b_star and a_circle == b_circle and a_square > b_square:
        answer.append("A")
    elif a_star == b_star and a_circle == b_circle and a_square < b_square:
        answer.append("B")
    elif a_star == b_star and a_circle == b_circle and a_square == b_square and a_triangle > b_triangle:
        answer.append("A")
    elif a_star == b_star and a_circle == b_circle and a_square == b_square and a_triangle < b_triangle:
        answer.append("B")
    else:
        answer.append("D")

for ans in answer:
    print(ans)
