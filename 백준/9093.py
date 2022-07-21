t = int(input())

for _ in range(t):
    sentence = input()
    sentence += " "
    stack = []
    for word in sentence:
        if word == " ":
            while stack:
                print(stack.pop(), end='')
            print(" ", end='')

        else:
            stack.append(word)
