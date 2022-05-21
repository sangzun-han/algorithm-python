t = int(input())

data = [int(x) for x in input().strip().split()]
data.sort()

print(data[len(data)//2])
