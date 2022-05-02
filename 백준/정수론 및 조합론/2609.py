import sys

n, m = map(int, sys.stdin.readline().split())
min_value = min(n, m)
gcd = []

for i in range(2, min_value+1):
    if n % i == 0 and m % i == 0:
        gcd.append(i)

if len(gcd) != 0:
    print(gcd[-1])
    print(round((n / gcd[-1]) * (m / gcd[-1]) * gcd[-1]))
else:
    print(1)
    print(n*m)
