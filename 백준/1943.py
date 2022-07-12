t = int(input())

def gcd(a,b):
    while a%b != 0:
        r = a % b
        a = b
        b = r
    return b

for _ in range(t):
    a,b = map(int, (input()).split())
    ans = gcd(a,b)
    print(a*b//ans)

