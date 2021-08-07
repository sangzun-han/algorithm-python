C = int(input())
for i in range(C):
    stu = list(map(int, input().split()))
    avg = sum(stu[1:])/stu[0]
    cnt = 0
    for score in stu[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/stu[0]*100
    print('{:.3f}%'.format(rate))
