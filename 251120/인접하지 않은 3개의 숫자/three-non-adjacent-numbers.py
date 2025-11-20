n = int(input())

nums = list(map(int, input().split()))

max_num_lefts = [0] * n
max_num_rights = [0] * n

max_num_lefts[0] = nums[0]
for i in range(1, n):
    max_num_lefts[i] = max(max_num_lefts[i - 1], nums[i])

max_num_rights[n - 1] = nums[n - 1]
for i in range(n - 2, -1, -1):
    max_num_rights[i] = max(max_num_rights[i + 1], nums[i])

ret = 0
for j in range(2, n - 2):
    left_max = max_num_lefts[j - 2]
    right_max = max_num_rights[j + 2]
    ret = max(ret, left_max + right_max + nums[j])
print(ret)
