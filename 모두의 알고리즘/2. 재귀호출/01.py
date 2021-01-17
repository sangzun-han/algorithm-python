# Factorial

def fact(num):
    fac = 1
    for index in range(1,num+1):
        fac = fac*index
    return fac

def recursive(num):
    if num < 1:
        return 1
    else:
        return num * recursive(num-1)

# 1부터 n까지의 합 
def sum(num):
    if num == 0:
        return 0
    else:
        return num + sum(num-1)

# 숫자 n개 중 최대값 찾기
def findMax(lists, n):
    if n==1:
        return lists[0]
    else:
        maxnum = findMax(lists, n-1)
    if maxnum > lists[n-1]:
        return maxnum
    else:
        return lists[n-1]

v = [17,11,82,40]
print(findMax(v, len(v)))
