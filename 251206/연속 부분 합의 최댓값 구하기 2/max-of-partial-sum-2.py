n = int(input())

nums = list(map(int, input().split()))

max_substr_sum = max(nums)
prev_sum = 0
prev_cnt = 0
for i in range(n):
    if nums[i] < 0:
        if prev_cnt > 0:
            max_substr_sum = max(max_substr_sum, prev_sum)
        prev_sum = 0
        prev_cnt = 0
    else:
        prev_sum += nums[i]
        prev_cnt += 1
if prev_cnt > 0:
    max_substr_sum = max(max_substr_sum, prev_sum)
print(max_substr_sum)
