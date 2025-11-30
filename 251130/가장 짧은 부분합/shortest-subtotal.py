n, target_sum = map(int, input().split())

numbers = list(map(int, input().split()))

cur_sum = 0
j = 0
ans = float("inf")
for i in range(n):
    while j + 1 <= n and cur_sum < target_sum:
        cur_sum += numbers[j]
        j += 1

    ans = min(ans, j - i + 1)
    cur_sum -= numbers[i]

print(ans)
