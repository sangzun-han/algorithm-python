for tc in range(10):
    length = int(input())  # 원본 암호문 길이
    pwd = list(map(int, input().split()))  # 원본 암호문
    count = int(input())  # 명령어 개수
    cmd = list(input().split())  # 명령어

    for i in range(len(cmd)):
        if cmd[i] == 'I':
            pos = int(cmd[i+1])
            repeat = int(cmd[i+2])
            for j in range(repeat):
                pwd.insert(pos+j, int(cmd[i+j+3]))
        elif cmd[i] == 'D':
            pos = int(cmd[i+1])
            repeat = (int(cmd[i+2]))
            for j in range(repeat):
                del pwd[pos]

    print(f"#{tc+1}", end=' ')
    for i in range(10):
        print(pwd[i], end=' ')
    print()
