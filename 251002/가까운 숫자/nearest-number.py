from sortedcontainers import SortedSet

n=int(input())

s=SortedSet()
s.add(0)

min_len=10**9
ret=[]
num_list=list(map(int, input().split()))
for i in range(n):
    num=num_list[i]
    if len(s)==1:
        min_len=num
        ret.append(min_len)
        s.add(num)
    else:
        r_idx=s.bisect_right(num)
        if r_idx<len(s):
            right_num=s[r_idx]
        else:
            right_num=10**12
        left_num=s[r_idx-1]
        min_len=min(min_len, min(abs(right_num-num), abs(num-left_num)))
        ret.append(min_len)
        s.add(num)


print("\n".join(map(str, ret)))

