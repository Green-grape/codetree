from sortedcontainers import SortedSet

n, t = map(int, input().split())

s = SortedSet()

for _ in range(n):
    start_pos, v = map(int, input().split())
    end_pos = start_pos + v * t
    if len(s) == 0 or end_pos > s[-1]:
        s.add(end_pos)
    else:
        #print(end_pos, s)
        idx = s.bisect_left(end_pos)
        s.remove(s[idx])
        s.add(end_pos)

print(len(s))


# 0->3
# 1->7

# 2->11
# 3->9 => # 3->9
# 6->9
