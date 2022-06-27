dict = {
    "c=": "q",
    "c-": "q",
    "dz=": "q",
    "d-": "q",
    "lj": "q",
    "nj": "q",
    "s=": "q",
    "z=": "q",
}

word = input()
ans = 0
for key, value in dict.items():
    if key in word:
        word = word.replace(key, value)

print(len(word))
