import sys

input=sys.stdin.readline

n, m=map(int, input().split())

boards=[]
for i in range(n):
    boards.append(list(map(int, input().split())))

dp=[[-1]*m for _ in range(n)]

def get_max_jump(i, j):
    # i, j에서 시작해서 조건을 만족하면서 밟을 수 있는 최대 칸수를 반환한다.
    if dp[i][j]!=-1:
        return dp[i][j]
    if i==(n-1) and j==(m-1):
        return 1
    dp[i][j]=1
    for y in range(i+1, n):
        for x in range(j+1, m):
            if boards[i][j]<boards[y][x]:
                dp[i][j]=max(dp[i][j], 1+get_max_jump(y, x))
    return dp[i][j]


print(get_max_jump(0, 0))