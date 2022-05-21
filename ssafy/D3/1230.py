for tc in range(10):
    answer = []
    length = int(input())  # 암호문 길이
    pwds = list(map(int, input().split()))  # 원본 암호문
    count = int(input())  # 명령어 개수
    cmd = list(map(str, input().split()))  # 명령어

    for i in range(len(cmd)):
        if cmd[i] == 'I':
            idx = int(cmd[i+1])
            repeat = int(cmd[i+2])
            for j in range(repeat):
                pwds.insert(idx+j, cmd[i+j+3])
        elif cmd[i] == 'D':
            idx = int(cmd[i+1])
            repeat = int(cmd[i+2])
            for j in range(repeat):
                del pwds[idx]
        elif cmd[i] == 'A':
            repeat = int(cmd[i+1])
            for j in range(1, repeat+1):
                pwds.append(cmd[i+j+1])
    print(f'#{tc+1}', end=' ')
    for idx, pwd in enumerate(pwds):
        if idx == 10:
            break
        print(f"{pwd}", end=' ')
    print()
