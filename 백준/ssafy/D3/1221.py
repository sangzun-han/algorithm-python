dict1 = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

dict2 = {
    0: "ZRO",
    1: "ONE",
    2: "TWO",
    3: "THR",
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN"
}

t = int(input())

for t in range(t):
    tc, length = map(str, input().split())
    length = int(length)
    numbers = list(map(str, input().split()))
    answer = []
    for number in numbers:
        answer.append(dict1[number])
    answer.sort()
    numbers.clear()
    for answer in answer:
        numbers.append(dict2[answer])

    print(f"{tc}")
    for number in numbers:
        print(number, end=' ')
