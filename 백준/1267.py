n = int(input())
phone = list(map(int, input().split()))
y, m = 0, 0
for i in range(n):
    y += ((phone[i] // 30) + 1) * 10
    m += ((phone[i] // 60) + 1) * 15

if y == m:
    print(f"Y M {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y {y}")
