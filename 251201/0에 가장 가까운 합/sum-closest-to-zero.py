n = int(input())
nums = list(map(int, input().split()))

nums.sort()

i = 0
j = n - 1
best = float("inf")

while i < j:
    s = nums[i] + nums[j]
    if abs(s) < abs(best):
        best = s
    if s < 0:
        i += 1
    else:
        j -= 1
print(abs(best))
