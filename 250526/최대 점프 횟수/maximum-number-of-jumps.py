import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

dp=[-1]*n

def get_max_jump_cnt(i):
    # i번째부터 끝까지 점프 가능한 최대횟수 반환
    if dp[i]!=-1:
        return dp[i]
    if i==(n-1):
        return 0
    jump=nums[i]
    dp[i]=0
    for idx in range(i+1, min(i+jump+1, n)):
        dp[i]=max(dp[i], 1+get_max_jump_cnt(idx))
    return dp[i]

print(get_max_jump_cnt(0))