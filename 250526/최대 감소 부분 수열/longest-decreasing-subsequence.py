import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

dp=[-1]*n

def find_max_len_of_decreasing_seq(i):
    if dp[i]!=-1:
        return dp[i]
    if i==(n-1):
        return 1
    dp[i]=1
    for idx in range(i+1, n):
        if nums[i]>nums[idx]:
            dp[i]=max(dp[i], find_max_len_of_decreasing_seq(idx)+1)
    return dp[i]

ret=0
for idx in range(n):
    ret=max(ret, find_max_len_of_decreasing_seq(idx))
print(ret)
