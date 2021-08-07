num = int(input())
cnt = 0
result = num
while(True):
    a = num//10
    b = num % 10
    c = (a+b) % 10
    d = (b*10)+c
    num = d
    cnt += 1
    if(d == result):
        break

print(cnt)
