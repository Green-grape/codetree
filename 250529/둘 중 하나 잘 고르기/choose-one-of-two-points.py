import sys

input=sys.stdin.readline

n=int(input())

boards=[tuple(map(int, input().split())) for _ in range(2*n)]

dp=[[[-1]*(n+1) for _ in range(n+1)] for _ in range(2*n+1)]

def get_max_sum(i, j, k):
    # 현재 i번째에서 선택을 해야하고 현재까지 빨간색을 j번 선택, 피란색을 k번 선택했다면 이후에 잘 고른 최대합은?
    if i==2*n:
        return 0
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    if j!=n:
        dp[i][j][k]=max(dp[i][j][k], boards[i][0]+get_max_sum(i+1, j+1, k))
    if k!=n:
        dp[i][j][k]=max(dp[i][j][k], boards[i][1]+get_max_sum(i+1, j, k+1))
    return dp[i][j][k]

print(get_max_sum(0, 0, 0))