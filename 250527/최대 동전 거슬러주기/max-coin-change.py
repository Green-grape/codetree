import sys

input=sys.stdin.readline

n, m=map(int, input().split())

coins=list(map(int, input().split()))

def find_max_kind(m):
    dp=[-1]*(m+1)
    dp[0]=0
    for val in range(1, m+1):
        for coin in coins:
            if val>=coin and dp[val-coin]!=-1:
                dp[val]=max(dp[val], dp[val-coin]+1)
    return dp[m]

print(find_max_kind(m))