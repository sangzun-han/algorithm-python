# 선택정렬
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(n):
        if a[i]<a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a) # 최소값 위치
        value = a.pop(min_idx) # 
        result.append(value) # 최소값 append
    return result
    
# 선택정렬
def sel_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j] > a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx], a[i]

# 삽입정렬
def find_ins_idx(r,v):
    for i in range(len(r)):
        if v<r[i]:
            return i
        return len(r)

def ins_sort(a):
    result=[]
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result,value)
        result.insert(ins_idx, value)
    return result

def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key

# 병합 정렬
def merge_sort2(a):
    n = len(a)
    if n<=1:
        return a
    else:
        mid = n//2
        g1 = merge_sort(a[:mid])
        g2 = merge_sort(a[mid:])
        result = []
        while g1 and g2:
            if(g1 < g2):
                result.append(g1.pop(0))
            else:
                result.append(g2.pop(0))
        while g1:
            result.append(g1.pop(0))
        while g2:
            result.append(g2.pop(0))
        return result


# 병합정렬
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1<len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 <len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

# 퀵 정렬
def quick_sort(a):
    n = len(a)
    if n<=1:
        return a
    else:
        standard = a[-1]
        g1 = []
        g2 = []
        for index in range(0,n-1):
            if a[index] < standard:
                g1.append(a[index])
            else:
                g2.append(a[index])
        return quick_sort(g1) + [standard] + quick_sort(g2)

# 퀵 정렬
def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return 
    else:
        standard = a[end]
        i = start
        for j in range(start,end):
            if a[j] <= standard:
                a[i],a[j] = a[j],a[i]
                i += 1
        a[i],a[end] = a[end], a[i]
        
        quick_sort_sub(a,start, i-1)
        quick_sort_sub(a,i+1,end)

def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1)


# 버블정렬
def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0,n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i],a[i+1] = a[i+1],a[i]
                changed = True
        if changed == False:
            return a

# 이분 탐색
def binary_search(a,x):
    start = 0
    end = len(a) -1
    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# 재귀 이분 탐색
def binary_search_sub(a,x,start,end):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            return binary_search_sub(a,x,mid+1,end)
        else:
            return binary_search_sub(a,x,start,mid-1)
    return -1


