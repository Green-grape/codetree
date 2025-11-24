n, q = map(int, input().split())

nums = list(map(int, input().split()))

left_max = [0] * n
right_max = [0] * n

for i in range(1, n):
    left_max[i] = max(left_max[i - 1], nums[i - 1])

for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], nums[i + 1])

ret = []
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ret.append(str(max(left_max[l], right_max[r])))
print("\n".join(ret))
