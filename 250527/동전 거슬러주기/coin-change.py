import sys

n, m=map(int, input().split())

coin_values=list(map(int, input().split()))

dp=[10001]*(m+1)

def get_min_coin(cash):
    if dp[cash]!=10001:
        return dp[cash]
    if cash==0:
        return 0
    for coin_value in coin_values:
        if coin_value<=cash:
            cand_cnt=get_min_coin(cash-coin_value)
            if cand_cnt!=10001:
                dp[cash]=min(dp[cash], cand_cnt+1)
    return dp[cash]

ret=get_min_coin(m)
print(ret if ret!=10001 else -1)