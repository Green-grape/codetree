from sortedcontainers import SortedSet

n, m=map(int, input().split())

num_set=SortedSet(map(int, input().split()))

ret=[]
for _ in range(m):
    val=int(input())
    idx=num_set.bisect_left(val)
    if idx<len(num_set) and num_set[idx]>=val:
        ret.append(num_set[idx])
    else:
        ret.append(-1)

print("\n".join(map(str, ret)))
