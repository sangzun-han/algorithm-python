word = str(input().upper())
length = len(word)
dict = {}
ans = []
for i in range(length):
    if word[i] in dict:
        dict[word[i]] += 1
    else:
        dict[word[i]] = 1

max_value = max(dict.values())

for key, value in dict.items():
    if max_value == value:
        ans.append(key)

if len(ans) == 1:
    print(ans[0])
else:
    print("?")
