import sys

input=sys.stdin.readline

n, target_sum=map(int, input().split())

nums=list(map(int, input().split()))

dp=[[-1]*(41) for _ in range(n)]

def get_max_sum(i, cur_sum):
    # 이번에 i-1번까지 합이 cur_sum일때 끝까지 수행해서 target_sum이 되는 경우의 수는?
    if i==n and cur_sum==target_sum:
        return 1
    elif i==n:
        return 0
    if dp[i][cur_sum+20]!=-1:
        return dp[i][cur_sum+20]
    dp[i][cur_sum+20]=0
    if -20<=(cur_sum-nums[i])<=20:
        dp[i][cur_sum+20]+=get_max_sum(i+1, cur_sum-nums[i])
    if -20<=(cur_sum+nums[i])<=20:
        dp[i][cur_sum+20]+=get_max_sum(i+1, cur_sum+nums[i])
    return dp[i][cur_sum+20]

print(get_max_sum(0, 0))