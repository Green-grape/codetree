import sys

input=sys.stdin.readline

jewel_cnt, max_weight=map(int, input().split())

jewels=[tuple(map(int, input().split())) for _ in range(jewel_cnt)]

def get_max_jewel_value_sum(weight):
    dp=[-1]*(weight+1)
    dp[0]=0
    for jewel in jewels:
        for w in range(weight, 1, -1):
                if w>=jewel[0] and dp[w-jewel[0]]!=-1:
                    dp[w]=max(dp[w], dp[w-jewel[0]]+jewel[1])
    return max(dp)


print(get_max_jewel_value_sum(max_weight))