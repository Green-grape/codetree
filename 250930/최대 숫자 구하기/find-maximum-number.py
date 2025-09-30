from sortedcontainers import SortedSet

n, m=map(int, input().split())

s=SortedSet(range(1, m+1))

ret=[]
vals=list(map(int, input().split()))
for i in range(n):
    s.remove(vals[i])
    ret.append(s[-1])

print("\n".join(map(str, ret)))