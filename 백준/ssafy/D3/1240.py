for tc in range(10):
    count, pwd = map(str, input().split())
    pwd = list(pwd)
    idx = 0
    while True:
        if pwd[idx] == pwd[idx+1]:
            del pwd[idx]
            del pwd[idx]
            idx = 0
        else:
            idx += 1
            if len(pwd) == idx+1:
                break
    print(f"#{tc+1}", end=' ')
    for pwd in pwd:
        print(pwd, end='')
    print()
