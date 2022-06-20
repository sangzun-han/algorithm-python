t = int(input())
for tc in range(t):
    n = int(input())
    answer = "impossible"
    i = 2
    while True:
        temp = list(str(n*i))
        i += 1

        if len(temp) != len(str(n)):
            break

        if set(temp) == set(str(n)):
            answer = "possible"
            break
    print(f"#{tc+1} {answer}")
