from sortedcontainers import SortedSet

n, q = map(int, input().split())

nums = map(int, input().split())

sorted_set = SortedSet()

for i, num in enumerate(nums):
    sorted_set.add((num, i + 1))

ret = []
for _ in range(q):
    a, b = map(int, input().split())
    start = sorted_set.bisect_left((a, 0))
    end = sorted_set.bisect_right((b, n + 1))
    ret.append(str(end - start))
print("\n".join(ret))
