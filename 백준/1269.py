n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = set(a)
b = set(b)

c = a.difference(b)
d = b.difference(a)

print(len(c) + len(d))
