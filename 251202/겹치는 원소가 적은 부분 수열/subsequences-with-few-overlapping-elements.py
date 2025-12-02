n, k = map(int, input().split())

nums = list(map(int, input().split()))

count_dict = {}

j = 0
max_subarray_length = 0
for i in range(n):
    while j < n and (nums[j] not in count_dict or count_dict[nums[j]] < k):
        count_dict[nums[j]] = count_dict.get(nums[j], 0) + 1
        j += 1
    max_subarray_length = max(max_subarray_length, j - i)
    count_dict[nums[i]] -= 1

print(max_subarray_length)
