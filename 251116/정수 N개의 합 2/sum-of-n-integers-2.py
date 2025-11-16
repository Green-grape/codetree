n, k = map(int, input().split())

nums = list(map(int, input().split()))

sum_nums = sum(nums[:k])

max_sum = sum_nums
cur_sum = sum_nums
for i in range(k, n):
    cur_sum += nums[i] - nums[i - k]
    if cur_sum > max_sum:
        max_sum = cur_sum
print(max_sum)
