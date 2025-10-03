from sortedcontainers import SortedSet

n, m=map(int, input().split())

s=SortedSet()
s_r=SortedSet(key=lambda x:-x)

ret=2*(10**9)+1
for _ in range(n):
    num=int(input())
    if len(s)==1:
        ret=abs(num-s[0]) if abs(num-s[0])>=m else ret
    elif len(s)>2:
        right_min_idx=s.bisect_left(num+m) # num+m보다 같거나 큰것
        left_max_idx=s_r.bisect_left(num-m) # num-m보다 같거나 작은것
        if right_min_idx<len(s):
            ret=min(ret, s[right_min_idx]-num)
        if left_max_idx<len(s_r):
            ret=min(ret, num-s[left_max_idx])
    s.add(num)
    s_r.add(num)

print(-1 if ret==(2*(10**9)+1) else ret)


