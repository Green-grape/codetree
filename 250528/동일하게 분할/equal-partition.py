import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))
total_sum=sum(nums)

dp=[False]*(1000*n+1)
dp[0]=True

for num in nums:
    for val in range(len(dp), num-1, -1):
        if dp[val-num]:
            dp[val]=True
            
if total_sum%2!=0:
    print('No')
else:
    print('Yes' if dp[total_sum//2] else 'No')