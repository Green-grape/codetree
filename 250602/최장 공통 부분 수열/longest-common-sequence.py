import sys
str_a=input()
str_b=input()

dp=[[0]*len(str_b) for _ in range(len(str_a))]

def get_max_superseq_cnt(i, j):
    # 현재 a에서는 i번째 b에서는 j번째 문자열을 확인할때 최장 공통 수열의 길이는?
    if i==0 and j==0:
        return 1 if str_a[i]==str_b[j] else 0
    if dp[i][j]!=0:
        return dp[i][j]
    if (i>0 and j>0) and str_a[i]==str_b[j]:
        dp[i][j]=1+get_max_superseq_cnt(i-1, j-1)
    if i>0:
        dp[i][j]=max(dp[i][j], get_max_superseq_cnt(i-1, j))
    if j>0:
        dp[i][j]=max(dp[i][j], get_max_superseq_cnt(i, j-1))
    return dp[i][j]

print(get_max_superseq_cnt(len(str_a)-1,len(str_b)-1))