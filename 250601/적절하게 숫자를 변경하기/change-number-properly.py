import sys

input=sys.stdin.readline

n, max_diff_cnt=map(int, input().split())

nums=list(map(int, input().split()))

dp=[[[-1]*5 for _ in range(max_diff_cnt+1)] for _ in range(n)]

def get_most_similar_num(i, j, k):
    '''
    지금 i번째를 고를 차례이고 지금까지 인접한 두 숫자가 다른 횟수가 j이며 
    이전에 고른 숫자가 k일때 최대 유사도 값은?
    '''
    if i==n:
        return 0
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    dp[i][j][k]=0
    for next_num in range(1, 5):
        if next_num!=k and j<max_diff_cnt:
            dp[i][j][k]=max(dp[i][j][k], (nums[i]==next_num)+get_most_similar_num(i+1, j+1, next_num))
        elif next_num==k:
            dp[i][j][k]=max(dp[i][j][k], (nums[i]==next_num)+get_most_similar_num(i+1, j, next_num))
    return dp[i][j][k]

ret=0
for num in range(1, 5):
    ret=max(ret, (num==nums[0])+get_most_similar_num(1, 0, num))
print(ret)