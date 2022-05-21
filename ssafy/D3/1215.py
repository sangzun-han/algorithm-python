for tc in range(10):
    n = int(input())  # 몇 글자 회문
    matrix = [list(map(str, input())) for _ in range(8)]
    length = 8
    count = 0
    for i in range(length):
        for j in range(8-n+1):
            temp = []
            for k in range(n):
                temp.append(matrix[i][j+k])
            if temp == temp[::-1]:
                count += 1

    for i in range(8-n+1):
        for j in range(length):
            temp = []
            for k in range(n):
                temp.append(matrix[i+k][j])
            if temp == temp[::-1]:
                count += 1

    print(f"#{tc+1} {count}")
