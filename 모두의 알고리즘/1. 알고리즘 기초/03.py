#최댓값 찾기
def searchMax(num):
    lens = len(num)
    max_arr = num[0]
    for index in range(lens):
        if max_arr < num[index]:
           max_arr = num[index]
    return max_arr

#최댓값 인덱스 위치
def searchIndex(num):
    lens = len(num)
    max_idx = 0
    for index in range(lens):
        if num[index] > num[max_idx]:
            max_idx = index
    return max_idx



#최솟값 구하기
def searchMin(num):
    lens = len(num)
    min_arr = num[0]
    for index in range(lens):
        if min_arr > num[index]:
            min_arr = num[index]
    return min_arr

#동명이인 찾기
def findSame(person):
    lens = len(person)
    result = set()
    for i in range(lens):
        for j in range(i+1, lens):
            if (person[i] == person[j]):
                result.add(person[i])
    return result

#n명중 두명을 뽑아 짝지을 수 있는 모든 조합
def makePair(person):
    lens = len(person)
    for i in range(lens):
        for j in range(i+1, lens):
            print(person[i],"/", person[j])

