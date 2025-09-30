from sortedcontainers import SortedSet

n, m = map(int, input().split())

num_pair = [tuple(map(int, input().split())) for _ in range(n)]
num_pair = SortedSet(num_pair)

ret = []
for _ in range(m):
    x, y = map(int, input().split())
    idx = num_pair.bisect_left((x, y))
    if idx < len(num_pair):
        ret.append(num_pair[idx])
    else:
        ret.append((-1, -1))

print("\n".join(f"{a} {b}" for a, b in ret))
