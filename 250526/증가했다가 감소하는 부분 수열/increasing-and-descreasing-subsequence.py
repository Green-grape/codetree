import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

dp1=[-1]*n
dp2=[-1]*n
def get_max_increasing_seq(i):
    # i번째까지 계속 증가하는 수열의 최대길이 반환
    if dp1[i]!=-1:
        return dp1[i]
    if i==0:
        return 1
    dp1[i]=1
    for idx in range(0, i):
        if nums[idx]<nums[i]:
            dp1[i]=max(dp1[i], 1+get_max_increasing_seq(idx))
    return dp1[i]


def get_max_decreasing_seq(i):
    #i번째 부터 계속 감소하는 수염의 최대길이를 반환
    if dp2[i]!=-1:
        return dp2[i]
    if i==(n-1):
        return 1
    dp2[i]=1
    for idx in range(i+1, n):
        if nums[idx]<nums[i]:
            dp2[i]=max(dp2[i], 1+get_max_decreasing_seq(idx))
    return dp2[i]

ret=0
for idx in range(0, n):
    ret=max(ret, get_max_increasing_seq(idx)+get_max_decreasing_seq(idx)-1)
print(ret)