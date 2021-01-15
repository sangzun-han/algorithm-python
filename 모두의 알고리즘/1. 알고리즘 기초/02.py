# 1부터 n까지의 합
def total(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return (sum)

def total(num):
    return num*(num+1) / 2

#1부터 n까지 제곱의합
def squared(num):
    sum = 0
    for i in range(1, num+1):
        sum += i*i
    return sum

def squared2(num):
    return num*(num+1)*(2*num+1)/6
    
