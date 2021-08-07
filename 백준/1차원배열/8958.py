n = int(input())
for i in range(n):
    OX = input()
    score = 0
    sScore = 0
    for j in OX:
        if j == 'O':
            score += 1
        else:
            score = 0
        sScore += score
    print(sScore)
