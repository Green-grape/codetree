n, k, b = map(int, input().split())

nums = [1] * (n + 1)

for _ in range(b):
    empty_num = int(input())
    nums[empty_num] = 0

cur_cnt = sum(nums[1 : k + 1])
max_cnt = cur_cnt

for i in range(k + 1, n + 1):
    cur_cnt += nums[i] - nums[i - k]
    max_cnt = max(max_cnt, cur_cnt)

print(k - max_cnt)
