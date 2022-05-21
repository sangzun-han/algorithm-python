t = int(input())
for tc in range(t):
    n = list(input())
    length = len(n)
    init = ['0'] * length
    count = 0
    for i in range(length):
        if n[i] != init[i]:
            count += 1
            if n[i] == '0':
                for j in range(i, length):
                    init[j] = '0'

            elif n[i] == '1':
                for j in range(i, length):
                    init[j] = '1'

    print(f"#{tc+1} {count}")
