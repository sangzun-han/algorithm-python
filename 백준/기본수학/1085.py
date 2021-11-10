def distance(x,y):
  return (x**2 + y**2)**0.5

def distance2(x,y,w,h):
  return ((w-x)**2 + (h-y)**2)**0.5


x,y,w,h = map(int, input().split())

a = distance(x,y)
b = distance2(x,y,w,h)

print(min(a,b,x,y,w-x,h-y))