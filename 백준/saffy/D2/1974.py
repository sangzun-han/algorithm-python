t = int(input())
for i in range(t):
    puzzle = []
    total_count = 0
    for j in range(9):

        data = list(map(int, input().split()))
        puzzle.append(data)

    for j in range(9):
        sample_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        count = 0
        for k in range(9):
            try:
                sample_puzzle.remove(puzzle[j][k])
            except:
                count += 1

        sample_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for l in range(9):
            try:
                sample_puzzle.remove(puzzle[l][j])
            except:
                count += 1
        if count >= 1:
            total_count += 1

        sample_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if j == 0 or j == 3 or j == 6:
            for o in range(3):
                try:
                    sample_puzzle.remove(puzzle[j][o])
                    sample_puzzle.remove(puzzle[j+1][o])
                    sample_puzzle.remove(puzzle[j+2][o])
                except:
                    count += 1
            if count >= 1:
                total_count += 1

    if total_count >= 1:
        print("#{} {}".format(i+1, 0))
    else:
        print("#{} {}".format(i+1, 1))
1
