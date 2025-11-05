from sortedcontainers import SortedSet

n, m = map(int, input().split())

num_list = map(int, input().split())
s = SortedSet(num_list, lambda x: -x)
cmd_list = list(map(int, input().split()))

ret = []
for i in range(m):
    target = s.bisect_left(cmd_list[i])
    if target < len(s):
        ret.append(s[target])
        s.remove(s[target])
    else:
        ret.append(-1)
print("\n".join(map(str, ret)))
