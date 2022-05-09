t = int(input())

for tc in range(t):
    n = int(input())
    line = 0
    alphabet = ''
    for i in range(n):
        c, k = map(str, input().split())
        alphabet += c*int(k)
    print("#{}".format(tc+1))
    if len(alphabet) <= 10:
        print(alphabet, end=' ')
    else:
        for j in range(len(alphabet) // 10 + 1):
            print(alphabet[10*j:10*j+10])
