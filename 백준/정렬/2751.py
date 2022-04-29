n = int(input())
temp = 0
arr = []
for _ in range(n):
    arr.append(int(input()))


def merge(left, right):
    i = 0
    j = 0
    sort_list = []

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sort_list.append(left[i])
            i += 1
        else:
            sort_list.append(right[j])
            j += 1

    while (i < len(left)):
        sort_list.append(left[i])
        i += 1

    while (j < len(right)):
        sort_list.append(right[j])
        j += 1

    return sort_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)


print('\n'.join(str(s) for s in merge_sort(arr)))
