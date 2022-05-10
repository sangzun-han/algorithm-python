t = int(input())

for tc in range(t):

    p, q, r, s, w = map(int, input().split())
    a_charge = 0
    b_charge = 0

    if w <= r:
        b_charge = q
        a_charge = p * w
    elif w > r:
        a_charge = p * w
        b_charge = q + ((w - r) * s)
    charge = min(a_charge, b_charge)

    print("#{} {}".format(tc+1, charge))
