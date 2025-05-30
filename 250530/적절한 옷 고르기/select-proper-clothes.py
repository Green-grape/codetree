import sys

n, m=map(int, input().split())

cloths=[tuple(map(int, input().split())) for _ in range(n)]

dp=[[-1]*(n+1) for _ in range(m)]

def get_max_content(i, j):
    # 현재 i번째날을 고를 차례이고 이전에 j번째 옷을 골랐을때 최종적인 만족도의 합
    if i==m:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j]=0
    for idx in range(n):
        if (cloths[idx][0]-1)<=i and i<=(cloths[idx][1]-1):
            cand=get_max_content(i+1, idx)
            if cand!=-1:
                dp[i][j]=max(dp[i][j], abs(cloths[j][2]-cloths[idx][2])+cand)
    return dp[i][j]

ret=0
for i in range(n):
    if cloths[i][0]<=1:
        ret=max(ret, get_max_content(1, i))
print(ret)