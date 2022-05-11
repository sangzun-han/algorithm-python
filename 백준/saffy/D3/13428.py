t = int(input())


def listToInt(lst):
    a = int(''.join(lst))
    return a


for tc in range(t):
    n = int(input())
    list_n = list(str(n))
    min, max = n, n
    for i in range(len(list_n)):
        for j in range(1, len(list_n)):
            temp = list_n[i]
            list_n[i] = list_n[j]
            list_n[j] = temp
            if (list_n[0] != "0") and (listToInt(list_n) < min):
                min = listToInt(list_n)
            if (list_n[0] != "0") and (listToInt(list_n) > max):
                max = listToInt(list_n)
            temp = list_n[i]
            list_n[i] = list_n[j]
            list_n[j] = temp

    print("#{} {} {}".format(tc+1, min, max))
