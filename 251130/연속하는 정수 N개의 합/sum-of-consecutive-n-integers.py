n, target_sum = map(int, input().split())

numbers = list(map(int, input().split()))

cur_sum = 0
j = 0
ans = 0
for i in range(n):
    while j < n and cur_sum < target_sum:
        cur_sum += numbers[j]
        j += 1
    if cur_sum == target_sum:
        ans += 1
    cur_sum -= numbers[i]

print(ans)
