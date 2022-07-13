n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()


def binary_search(num):
    start = 0  # 시작지점
    end = n-1  # 끝지점

    while start <= end:
        mid = (start+end) // 2
        if n_list[mid] == num:
            return 1
        elif n_list[mid] > num:
            end = mid - 1
        elif n_list[mid] < num:
            start = mid + 1
    return 0


for num in m_list:
    print(binary_search(num), end=' ')
