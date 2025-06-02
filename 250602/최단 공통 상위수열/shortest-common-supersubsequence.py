import sys
str_a=input()
str_b=input()

la=len(str_a)
lb=len(str_b)
str_a=" "+str_a
str_b=" "+str_b



dp=[[0]*(lb+1) for _ in range(la+1)]
dp[1][1]=1 if str_a[1]==str_b[1] else 2


#init
for i in range(2, la+1):
    if str_a[i]==str_b[1]:
        dp[i][1]=i
    else:
        dp[i][1]=dp[i-1][1]+1
for j in range(2, lb+1):
    if str_a[1]==str_b[j]:
        dp[1][j]=j
    else:
        dp[1][j]=dp[1][j-1]+1

for i in range(2, la+1):
    for j in range(2, lb+1):
        if str_a[i]==str_b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=min(dp[i-1][j], dp[i][j-1])+1
        

print(dp[la][lb])