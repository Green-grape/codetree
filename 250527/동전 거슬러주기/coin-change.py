import sys

sys.setrecursionlimit(100000)

n, m=map(int, input().split())

coin_values=list(map(int, input().split()))

def get_min_coin(cash):
    dp=[10001]*(cash+1)
    dp[0]=0
    for c in range(1, cash+1):
        for coin in coin_values:
            if c>=coin:
                if dp[c-coin]==10001:
                    continue
                dp[c]=min(dp[c], dp[c-coin]+1)
    return dp[cash]    

ret=get_min_coin(m)
print(ret if ret!=10001 else -1)