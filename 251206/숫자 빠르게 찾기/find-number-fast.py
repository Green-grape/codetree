n, m = map(int, input().split())

nums = list(map(int, input().split()))

ret = []
for _ in range(m):
    num = int(input())
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == num:
            ret.append(mid + 1)
            break
        elif nums[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    if l > r:
        ret.append(-1)

print("\n".join(map(str, ret)))
