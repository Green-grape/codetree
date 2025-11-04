from sortedcontainers import SortedSet

n, m = map(int, input().split())

cord_list = [tuple(map(int, input().split())) for _ in range(n)]

s = SortedSet(cord_list)

for _ in range(m):
    target_x = int(input())
    right_min_idx = s.bisect_right((target_x, 0))
    if right_min_idx == len(s):
        print(-1, -1)
    else:
        ans = s[right_min_idx]
        print(ans[0], ans[1])
        s.remove(ans)
