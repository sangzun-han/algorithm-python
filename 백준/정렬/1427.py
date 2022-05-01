n = int(input())
num_list = (list(str(n)))
num_list.sort(reverse=True)

for num in num_list:
    print(num, end='')
