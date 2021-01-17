# 재귀호출을 이용한 최대값 찾기

```
def findMax(lists, n):
    if n==1:
        return lists[0]
    else:
        maxnum = findMax(lists, n-1)
    if maxnum > lists[n-1]:
        return maxnum
    else:
        return lists[n-1]

v = [17,11,82,40]
print(findMax(v, len(v)))
```

<img width='400px' src="https://user-images.githubusercontent.com/57563053/104853825-b7bafd80-5946-11eb-99d9-0f255e88dbaf.gif">
