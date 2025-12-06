n = int(input())

nums = list(map(int, input().split()))

prev_sum = 0
max_substr_sum = -float("inf")
for i in range(n):
    prev_sum += nums[i]
    if prev_sum > max_substr_sum:
        max_substr_sum = prev_sum
    if prev_sum < 0:
        prev_sum = 0
print(max_substr_sum)
