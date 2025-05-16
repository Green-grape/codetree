n=int(input())

nums=list(map(int, input().split()))

total_sum=sum(nums)
cur_pos=[]

ret=total_sum
def find_min_diff(idx, cnt):
    global ret
    if cnt==n:
        cur_sum=sum([nums[i] for i in cur_pos])
        ret=min(ret, abs(total_sum-2*cur_sum))
        return
    if idx>=2*n:
        return
    cur_pos.append(idx)
    find_min_diff(idx+1, cnt+1)
    cur_pos.pop()
    find_min_diff(idx+1, cnt)


find_min_diff(0, 0)
print(ret)