n, m = map(int, input().split())
words = []
search_words = []
ans = 0
for _ in range(n):
    words.append(input())

for i in range(m):
    search_words.append(input())

for i in range(m):
    if search_words[i] in words:
        ans += 1

print(ans)
