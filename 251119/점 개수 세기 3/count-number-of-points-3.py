from bisect import bisect_left, bisect_right

n, q = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()


ret = []
for _ in range(q):
    a, b = map(int, input().split())
    start = bisect_left(nums, a)
    end = bisect_right(nums, b)
    ret.append(str(end - start))
print("\n".join(ret))
