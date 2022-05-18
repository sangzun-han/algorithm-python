# 시간초과
# t = int(input())
# answer = []
# for tc in range(t):
#     n = int(input())
#     mul = 1
#     while True:
#         if (n * mul) ** 0.5 == int((n * mul) ** 0.5):
#             answer.append(mul)
#             break
#         else:
#             mul += 1


# for idx, answer in enumerate(answer):
#     print("#{} {}".format(idx+1, answer))


t = int(input())
a = [False, False] + [True] * int(10000000**0.5)
prime = []
answer = []
for i in range(2, int(10000000**0.5)+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, int(10000000**0.5)+1, i):
            a[j] = False

for tc in range(t):
    n = int(input())
    result = 1
    if (n**0.5) != int(n**0.5):
        for p in prime:
            count = 0
            while not n % p:
                n //= p
                count += 1
            if count % 2:
                result *= p
            if n == 1 or p > n:
                break
        if n > 1:
            result *= n
    answer.append(result)

for idx, answer in enumerate(answer):
    print("#{} {}".format(idx+1, answer))
