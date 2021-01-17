# 하노이탑
# from에 num개의 원반을 by를 거쳐서 to로 이동
def Hanoi(num, from_pos, by, to):
    if num==1:
        print(from_pos, "->",to)
        return
    else:
        Hanoi(num-1, from_pos, to, by)
        print(from_pos, "->",to)
        Hanoi(num-1, by, from_pos, to)
