import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

MIN=n*-1000

dp=[MIN]*(n+1)
def get_max_successive_sum(i):
    # i번까지 보았을때 연속된 부분수열의 합의 최대
    if dp[i]!=MIN:
        return dp[i]
    dp[i]=nums[i]
    cur_sum=0
    for idx in range(i-1, -1, -1):
        cur_sum+=nums[idx+1]
        dp[i]=max(dp[i], get_max_successive_sum(idx)+cur_sum)
    return dp[i]

ret=MIN
for i in range(n):
    ret=max(ret, get_max_successive_sum(i))
print(ret)