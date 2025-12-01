n = int(input())

nums = list(map(int, input().split()))

nums.sort()

j = n - 1
cur_close_to_zero = float("inf")
most_close_to_zero = float("inf")
for i in range(n):
    prev_num = cur_close_to_zero
    while j > i and abs(nums[i] + nums[j]) <= abs(cur_close_to_zero):
        cur_close_to_zero = nums[i] + nums[j]
        if abs(cur_close_to_zero) > abs(prev_num):
            cur_close_to_zero = prev_num
            break
        j -= 1
    if abs(cur_close_to_zero) < abs(most_close_to_zero):
        most_close_to_zero = cur_close_to_zero

print(abs(most_close_to_zero))
