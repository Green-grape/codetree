n, m = map(int, input().split())

nums = list(map(int, input().split()))

cnt_dict = {}
for num in nums:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

ret = []
for _ in range(m):
    num = int(input())
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == num:
            ret.append(cnt_dict[num])
            break
        elif nums[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    if l > r:
        ret.append(0)

print("\n".join(map(str, ret)))
