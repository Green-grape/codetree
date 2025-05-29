import sys

input=sys.stdin.readline

n=int(input())

MOD=int(1e9+7)

def mod_sum(a, b):
    return (a%MOD+b%MOD)%MOD

dp=[[[-1]*3 for _ in range(3)] for _ in range(n)]

def get_life_string_cnt(life, t_cnt, b_suc_cnt):
    #현재 생존일수가 life이고 T의 개수가 t_cnt, 연속적인 B의 개수가 b_suc_cnt일때 n일까지 살아님기 위한 가짓수는?
    if life==n and t_cnt<3 and b_suc_cnt<3:
        return 1
    elif life==n:
        return 0
    if dp[life][t_cnt][b_suc_cnt]!=-1:
        return dp[life][t_cnt][b_suc_cnt]
    dp[life][t_cnt][b_suc_cnt]=0
    if t_cnt<2:
        dp[life][t_cnt][b_suc_cnt]=mod_sum(dp[life][t_cnt][b_suc_cnt], get_life_string_cnt(life+1, t_cnt+1, 0))
    if b_suc_cnt<2:
        dp[life][t_cnt][b_suc_cnt]=mod_sum(dp[life][t_cnt][b_suc_cnt], get_life_string_cnt(life+1, t_cnt, b_suc_cnt+1))
    dp[life][t_cnt][b_suc_cnt]=mod_sum(dp[life][t_cnt][b_suc_cnt], get_life_string_cnt(life+1, t_cnt, 0))
    return dp[life][t_cnt][b_suc_cnt]

print(get_life_string_cnt(0, 0, 0))