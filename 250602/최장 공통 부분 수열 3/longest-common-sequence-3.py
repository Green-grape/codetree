import sys

input=sys.stdin.readline

la, lb=map(int, input().split())

arr_a=list(map(int, input().split()))
arr_b=list(map(int, input().split()))

dp=[[-1]*(lb+1) for _ in range(la+1)]
dp[0][0]=0

for i in range(la+1):
    for j in range(lb+1):
        if dp[i][j]==-1:
            continue
        if i<la and j<lb and arr_a[i]==arr_b[j]:
            dp[i+1][j+1]=max(dp[i+1][j+1], 1+dp[i][j])
        if i<la:
            dp[i+1][j]=max(dp[i+1][j], dp[i][j])
        if j<lb:
            dp[i][j+1]=max(dp[i][j+1], dp[i][j])

i, j=la, lb
ret=[]
while i>0 and j>0:
    if arr_a[i-1]==arr_b[j-1]:
        ret.insert(0, arr_a[i-1])
        i-=1
        j-=1
    elif dp[i-1][j]==dp[i][j-1]:
        if arr_a[i-1]>arr_b[j-1]: i-=1
        else: j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1

print(" ".join([str(num) for num in ret]))