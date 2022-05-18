def intJudgment(n):
    answer = False
    num = n**0.5

    if num == int(num):
        answer = True
    else:
        answer = False
    return answer


t = int(input())

for tc in range(t):
    a, b = map(int, input().split())

    count = 0
    for i in range(a, b+1):
        palindrome = True
        num_str = str(i)
        list_num_str = list(num_str)
        for j in range(len(str(i))//2):
            if list_num_str[j] != list_num_str[-1-j]:
                palindrome = False
                break

        if palindrome and intJudgment(i):
            root = str(int(i**0.5))
            list_root = list(root)
            for j in range(len(root)//2):
                if list_root[j] != list_root[-1-j]:
                    palindrome = False
                    break
        else:
            palindrome = False
        if palindrome:
            count += 1
    print("#{} {}".format(tc+1, count))
