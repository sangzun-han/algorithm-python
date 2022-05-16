t = int(input())

for tc in range(t):
    n = int(input())
    matrix = []
    row_check, col_check, left_diag_check, right_diag_check = False, False, False, False
    for i in range(n):
        temp = list(input())
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'o':
                count = 1
                for k in range(1, 5):
                    if i+k >= n:
                        break
                    if matrix[i+k][j] == 'o':
                        count += 1
                    else:
                        count = 0
                if count >= 5:
                    row_check = True
                    break
        for j in range(n):
            if matrix[j][i] == 'o':
                count = 1
                for k in range(1, 5):
                    if i+k >= n:
                        break
                    if matrix[j][i+k] == 'o':
                        count += 1
                    else:
                        count = 0
                if count >= 5:
                    col_check = True
                    break

        for j in range(n):
            if matrix[i][j] == 'o':
                count = 1
                for k in range(1, 5):
                    if i+k >= n or j-k < 0:
                        break
                    if matrix[i+k][j-k] == 'o':
                        count += 1
                    else:
                        count = 0
                if count >= 5:
                    left_diag_check = True
                    break

        for j in range(n):
            if matrix[i][j] == 'o':
                count = 1
                for k in range(1, 5):
                    if i+k >= n or j+k >= n:
                        break
                    if matrix[i+k][j+k] == 'o':
                        count += 1
                    else:
                        count = 0
                if count >= 5:
                    right_diag_check = True
                    break

    if row_check or col_check or left_diag_check or right_diag_check:
        print("#{} {}".format(tc+1, "YES"))
    else:
        print("#{} {}".format(tc+1, "NO"))
