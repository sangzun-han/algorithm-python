t = int(input())

for i in range(t):
    word = str(input())
    count = 0
    for j in range(len(word)):
        if word[j] == word[len(word) - j-1]:
            count += 1
    if count == len(word):
        print("#{} 1".format(i+1))
    else:
        print("#{} 0".format(i+1))
