# 최대공약수
def gcd(num1,num2):
    num = min(num1,num2)
    while True:
        if (num1 % num == 0) and (num2 % num == 0):
            return num
        num = num-1

# 유클리드 알고리즘
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)


# 피보나치
def fibo(num):
    if num <= 1:
        return num
    elif (num == 0):
        return 0
    else:
        return fibo(num-2) + fibo(num-1)


print(fibo(10))