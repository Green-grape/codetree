import sys

input=sys.stdin.readline

jewel_cnt, total_weight=map(int, input().split())

jewels=[tuple(map(int, input().split())) for _ in range(jewel_cnt)]

def get_max_jewel_value(weight):
    dp=[-1]*(weight+1)
    dp[0]=0
    for w in range(1, weight+1):
        for jewel in jewels:
            if w>=jewel[0] and dp[w-jewel[0]]!=-1:
                dp[w]=max(dp[w], dp[w-jewel[0]]+jewel[1])
    return max(dp)

print(get_max_jewel_value(total_weight))