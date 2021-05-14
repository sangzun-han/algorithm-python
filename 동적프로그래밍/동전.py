import sys

K = int(sys.stdin.readline())     # 교환할 금액
Coins = [1,4,7,13,28,52,91,365]     # 화폐의 종류
count = 0                           # 동전의 개수

for i in range(1,len(Coins)+1):  # 동전의 종류만큼 나누어가기 위해 동전의 종류의 수만큼 반복
    coin = Coins[-i]                # 가장 큰 화폐 단위부터 나누어가기 위한 인덱스의 끝부터 시작
    if K >= coin :                # 화폐의 단위가 구하려는 금액보다 작거나 같다면
        num = K // coin           # 합계를 화폐의 단위로 나누어서 몫을 구한다.
        K -= coin * num   # 구한 몫을 사용하여 화폐의 단위와 곱하여 합계에서 뺀다.
        count += num                # 그리고 구한 몫을 동전의 개수라고 생각하여 Count에 더한다.
                                    # 위와 같은 연산을 인덱스의 수만큼 진행하여 동전의 개수를 구한다.
                                
print(count)
