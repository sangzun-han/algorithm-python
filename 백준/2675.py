t = int(input())

for _ in range(t):
    r, s = map(str, input().split())

    for i in range(len(s)):
        print(f"{s[i]*int(r)}", end='')
    print()
