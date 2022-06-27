a, b = map(list, input().split())

a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]

a = ''.join(str(s) for s in a)
b = ''.join(str(s) for s in b)

print(max(int(a), int(b)))
