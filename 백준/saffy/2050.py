t = str(input())
alphabet = list(t)

for i in range(len(alphabet)):
    print(ord(alphabet[i])-64, end=' ')
