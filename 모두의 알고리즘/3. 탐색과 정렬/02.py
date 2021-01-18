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