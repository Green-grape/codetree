n, k = map(int, input().split())

MAX_NUM = 1000000
count_in_k = [0] * (MAX_NUM + 1)
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

max_num = -1
for i, num in enumerate(nums):
    count_in_k[num] += 1
    if i - k > 0:
        count_in_k[nums[i - k - 1]] -= 1
    if count_in_k[num] >= 2:
        max_num = max(max_num, num)
print(max_num)
