import sys

str_a=input()
str_b=input()

la=len(str_a)
lb=len(str_b)

dp=[[sys.maxsize]*(lb+1) for _ in range(la+1)]
dp[0][0]=0

for i in range(la+1):
    for j in range(lb+1):
        if dp[i][j]==sys.maxsize:
            continue
        if i<la and j<lb and str_a[i]==str_b[j]:
            dp[i+1][j+1]=min(dp[i+1][j+1], dp[i][j])

        #삽입
        if i<la:
            dp[i+1][j]=min(dp[i+1][j], 1+dp[i][j])
        #삭제
        if j<lb:
            dp[i][j+1]=min(dp[i][j+1], 1+dp[i][j])

print(dp[la][lb])