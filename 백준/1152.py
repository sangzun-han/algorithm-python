n = str(input().strip())
count = 0
for str in n:
    if str == ' ':
        count += 1

print(0 if len(n) == 0 else count+1)
