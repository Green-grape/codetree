import sys

input=sys.stdin.readline

n=int(input())

abilities=[tuple(map(int, input().split())) for _ in range(n)]

MAX_S=11
MAX_B=9

dp=[[[-1]*(MAX_B+1) for _ in range(MAX_S+1)] for _ in range(n)]

def get_max_abilities_sum(i, s_cnt, b_cnt):
    if i==n:
        if not (s_cnt==MAX_S and b_cnt==MAX_B):
            return -2
        return 0
    if dp[i][s_cnt][b_cnt]>-1:
        return dp[i][s_cnt][b_cnt]
    dp[i][s_cnt][b_cnt]=0
    if s_cnt<MAX_S:
        cand=get_max_abilities_sum(i+1, s_cnt+1, b_cnt)
        if cand>-1:
            dp[i][s_cnt][b_cnt]=max(dp[i][s_cnt][b_cnt], abilities[i][0]+cand)
    if b_cnt<MAX_B:
        cand=get_max_abilities_sum(i+1, s_cnt, b_cnt+1)
        if cand>-1:
            dp[i][s_cnt][b_cnt]=max(dp[i][s_cnt][b_cnt], abilities[i][1]+cand)
    cand=get_max_abilities_sum(i+1, s_cnt, b_cnt)
    if cand>-1:
        dp[i][s_cnt][b_cnt]=max(dp[i][s_cnt][b_cnt], cand)
    return dp[i][s_cnt][b_cnt]

print(get_max_abilities_sum(0, 0, 0)) 

