t = int(input())
for _ in range(t):
    zero = [1, 0]
    one = [0, 1]
    n = int(input())
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        for i in range(2, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
        print(zero[-1], one[-1])
