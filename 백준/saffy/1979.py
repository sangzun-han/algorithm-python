t = int(input())

for i in range(t):
    total_count = 0
    n, k = map(int, input().split())
    puzzle = []

    for j in range(n):
        data = list(map(int, input().split()))
        puzzle.append(data)

    for m in range(n):
        count = 0
        for l in range(n):
            if puzzle[m][l] == 1:
                count += 1
            elif puzzle[m][l] == 0:
                if count == k:
                    total_count += 1
                    count = 0
                elif count < k or count > k:
                    count = 0

        if count == k:
            total_count += 1
            count = 0
        elif count < k or count > k:
            count = 0

        for o in range(n):
            if puzzle[o][m] == 1:
                count += 1
            elif puzzle[o][m] == 0:
                if count == k:
                    total_count += 1
                    count = 0
                elif count < k or count > k:
                    count = 0
        if count == k:
            total_count += 1
            count = 0
        elif count < k or count > k:
            count = 0

    print("#{} {}".format(i+1, total_count))
