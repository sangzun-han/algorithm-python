w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = (p+t) % (w*2)
q = (q+t) % (h*2)

if p > w:
    p = 2 * w - p
if q > h:
    q = 2 * h - q

print(p, q)
