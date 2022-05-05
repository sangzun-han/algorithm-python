t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(t):
    n, k = map(int, input().split())
    total_grade = []

    for j in range(n):
        mid, final, assignment = list(map(int, input().split()))
        total = (mid * 0.35) + (final * 0.45) + (assignment * 0.2)
        total_grade.append(total)

    k_score = total_grade[k-1]
    total_grade.sort(reverse=True)
    div = n // 10
    final_k_score = total_grade.index(k_score) // div

    print("#{} {}".format(i+1, grade[final_k_score]))
