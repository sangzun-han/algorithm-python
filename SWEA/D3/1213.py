for _ in range(10):
    t = int(input())
    s = list(input())  # 찾는 문자열
    string = list(input())  # 주어진 문자열
    length = len(s)
    count = 0
    for i in range(len(string)-length+1):
        if (string[i:i+length]) == s:
            count += 1
    print(f"#{t} {count}")
