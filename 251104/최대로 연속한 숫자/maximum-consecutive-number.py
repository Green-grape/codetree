from sortedcontainers import SortedSet

n, m = map(int, input().split())

s_num = SortedSet()
s_pair = SortedSet()

s_pair.add((n + 1, 0, n))
nums=map(int, input().split())
for num in nums:
    if len(s_num) == 0:
        s_num.add(num)
        s_pair.add((num, 0, num - 1))
        s_pair.add((n - num, num + 1, n))
        s_pair.remove((n + 1, 0, n))
    else:
        idx = s_num.bisect_right(num)
        left = s_num[idx - 1] if idx > 0 else -1
        right = s_num[idx] if idx < len(s_num) else n + 1
        s_num.add(num)
        s_pair.remove((right - left - 1, left + 1, right - 1))
        if left + 1 <= num - 1:
            s_pair.add((num - left - 1, left + 1, num - 1))
        if num + 1 <= right - 1:
            s_pair.add((right - num - 1, num + 1, right - 1))
    print(s_pair[-1][0])
