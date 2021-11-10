while True:
  lists = []
  x,y,z = map(int, input().split())
  lists.append(x)
  lists.append(y)
  lists.append(z)
  lists.sort()
  x = lists[0]
  y = lists[1]
  z = lists[2]
  if x==0 and y==0 and z==0:
    break
  if (z**2 == (x**2+y**2)):
    print("right")
  else:
    print("wrong")