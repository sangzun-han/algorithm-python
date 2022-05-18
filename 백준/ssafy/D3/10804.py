t = int(input())

for tc in range(t):
    n = list(input())
    print("#{}".format(tc+1), end=' ')
    for i in range(len(n)):
        if n[len(n)-1-i] == 'b':
            print("d", end='')
        elif n[len(n)-1-i] == 'd':
            print("b", end='')
        elif n[len(n)-1-i] == 'p':
            print("q", end='')
        elif n[len(n)-1-i] == 'q':
            print("p", end='')
    print()
