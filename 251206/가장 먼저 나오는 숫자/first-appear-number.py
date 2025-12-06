n, m = map(int, input().split())

nums = list(map(int, input().split()))

first_pos_dict = {}
for i, num in enumerate(nums):
    if num not in first_pos_dict:
        first_pos_dict[num] = i

queries = map(int, input().split())

ret = []
for q in queries:
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == q:
            ret.append(first_pos_dict[q] + 1)
            break
        elif nums[mid] < q:
            l = mid + 1
        else:
            r = mid - 1
    if l > r:
        ret.append(-1)

print("\n".join(map(str, ret)))
