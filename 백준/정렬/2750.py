n = int(input())
temp = 0
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print('\n'.join(str(s) for s in arr))
