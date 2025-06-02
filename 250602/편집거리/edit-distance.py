import sys
str_a=input()
str_b=input()

dp=[[sys.maxsize]*(len(str_b)+1) for _ in range(len(str_a)+1)]
dp[0][0]=0

len_a=len(str_a)
len_b=len(str_b)

for i in range(len_a+1):
    for j in range(len_b+1):
        if dp[i][j]==sys.maxsize:
            continue
        if i<len_a and j < len_b and str_a[i]==str_b[j]:
            dp[i+1][j+1]=min(dp[i+1][j+1], dp[i][j])

        # 삽입
        if i<len_a:
            dp[i+1][j]=min(dp[i+1][j], 1+dp[i][j])
        # 제거
        if j<len_b:
            dp[i][j+1]=min(dp[i][j+1], 1+dp[i][j])
        # 교체
        if i<len_a and j<len_b:
            dp[i+1][j+1]=min(dp[i+1][j+1], 1+dp[i][j])

print(dp[len_a][len_b])