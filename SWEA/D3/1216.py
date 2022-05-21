def palindrome(n, m, matrix):


for _ in range(10):
    tc = int(input())
    matrix = [list(map(str, input())) for _ in range(100)]
    for m in range(100, -1, -1):
        if palindrome(100, m, matrix):
            break
