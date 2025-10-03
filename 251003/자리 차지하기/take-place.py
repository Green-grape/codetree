from sortedcontainers import SortedSet

n, m=map(int, input().split())

s=SortedSet(range(1, m+1), key=lambda x:-x)
num_list=map(int, input().split())

ret=0
for num in num_list:
    idx=s.bisect_left(num) # num보다 같거나 작은 원소의 위치
    if idx==len(s):
        if s[idx-1]>num:
            break
    ret+=1
    s.remove(s[idx])
print(ret)



