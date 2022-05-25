result = []
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x2 > p1 or x1 > p2 or q1 < y2 or q2 < y1:
        print("d")
        continue
    elif p1 == x2:
        if q1 == y2 or y1 == q2:
            print("c")
            continue
        else:
            print("b")
            continue
    elif x1 == p2:
        if y2 == q1 or y1 == q2:
            print("c")
            continue
        else:
            print("b")
            continue

    elif q1 == y2:
        if x1 == p2 or p1 == x2:
            print("c")
            continue
        else:
            print("b")
            continue
    elif y1 == q2:
        if x2 == p1 or x1 == p2:
            print("c")
            continue
        else:
            print("b")
            continue
    else:
        print("a")
