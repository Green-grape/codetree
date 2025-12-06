n, k = map(int, input().split())

nums = list(map(int, input().split()))

j = 0
cnt_one = 0
min_len = n + 1
for i in range(n):
    while j < n and cnt_one + (nums[j] == 1) <= k:
        if cnt_one == k and nums[j - 1] == 1:
            break
        cnt_one += nums[j] == 1
        j += 1
    if cnt_one >= k:
        min_len = min(min_len, j - i)
    cnt_one -= nums[i] == 1
print(min_len if min_len <= n else -1)
