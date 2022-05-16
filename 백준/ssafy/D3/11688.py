t = int(input())

for tc in range(t):
    nume, deno = 1, 1
    tree = list(str(input()))

    for i in tree:
        if i == 'L':
            deno += nume
        if i == 'R':
            nume += deno
    print("#{} {} {}".format(tc+1, nume, deno))
