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
    if i==0:
        return nums[i]
    dp[i]=max(nums[i], dp[i-1]+nums[i])
    return dp[i]

ret=MIN
for i in range(n):
    ret=max(ret, get_max_successive_sum(i))
print(ret)