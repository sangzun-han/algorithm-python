s = input()
ans = set()

for i in range(len(s)):
    for j in range(len(s)+1):
        if s[i:j]:
            ans.add(s[i:j])

print(len(ans))
