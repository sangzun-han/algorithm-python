a, b, c = map(int, input().split())

if a == b and b == c:
    print(f"{10000+a*1000}")
elif a == b:
    print(f"{1000+a*100}")
elif a == c:
    print(f"{1000+a*100}")
elif b == c:
    print(f"{1000+b*100}")
else:
    print(f"{max(a,b,c)*100}")
