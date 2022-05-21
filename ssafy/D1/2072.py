import sys

t = int(sys.stdin.readline())
case = []
for i in range(t):
    datas = list(map(int, sys.stdin.readline().split()))
    odd = [data for data in datas if data % 2 == 1]
    print("#{} {}".format(i+1, sum(odd)))

'''
정답
t = int(input())

for i in range(t):
    datas = list(map(int, input().split()))
    odd = [data for data in datas if data % 2 == 1]
    print("#{} {}".format(i+1, sum(odd)))

'''
