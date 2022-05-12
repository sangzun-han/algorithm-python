

t = int(input())
answer = []

for tc in range(t):
    a, b, c, d = map(int, input().split())
    on = min(b, d) - max(a, c)
    on = on if on > 0 else 0
    answer.append(on)

for idx, on in enumerate(answer):
    print("#{} {}".format(idx+1, on))
