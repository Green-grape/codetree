import sys

sys.setrecursionlimit(1000000)

n=int(input())

opponent=list(map(int, input().split()))
me=list(map(int, input().split()))

dp=[[-1]*n for _ in range(n)]

    
def get_max_num(i,j):
    # 상대의 맨 앞의 수가 i번째, 나의 맨 앞의 수가 j번째일때 게임이 끝났을때 얻을 수 있는 최대 점수는?
    if i==n or j==n: # 게임 종료
        return 0;
    if dp[i][j]!=-1:
        return dp[i][j]

    # 1번 rule
    dp[i][j]=0
    if opponent[i]>me[j]:
        dp[i][j]=max(dp[i][j], me[j]+get_max_num(i, j+1))
    elif opponent[i]<me[j]:
        dp[i][j]=max(dp[i][j], get_max_num(i+1, j))

    #2번 rule
    dp[i][j]=max(dp[i][j], get_max_num(i+1, j+1))
    return dp[i][j]

print(get_max_num(0, 0))

