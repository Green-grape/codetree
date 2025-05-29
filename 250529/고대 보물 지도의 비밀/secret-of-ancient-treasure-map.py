import sys

input=sys.stdin.readline

n, max_neg_num=map(int, input().split())

nums=list(map(int, input().split()))

dp=[[-sys.maxsize]*(max_neg_num+1) for _ in range(n)]

def get_min_dis(i, cur_neg_num):
    # 연속적으로 고른숫자의 마지막이 i-1번째 이고 현재까지 cur_neg_num만큼의 음수를 선택하였을때 합의 최대는?
    if dp[i][cur_neg_num]!=-sys.maxsize:
        return dp[i][cur_neg_num]
    if i==0:
        return nums[i]
    if not (nums[i]<0 and cur_neg_num>=max_neg_num):
        dp[i][cur_neg_num]=nums[i]
    if nums[i]<0:
        if cur_neg_num<max_neg_num:
            cand=get_min_dis(i-1, cur_neg_num+1)
            if cand!=-sys.maxsize:
                dp[i][cur_neg_num]=max(dp[i][cur_neg_num], nums[i]+cand)
    else:
        cand=get_min_dis(i-1, cur_neg_num)
        if cand!=-sys.maxsize:
            dp[i][cur_neg_num]=max(dp[i][cur_neg_num],nums[i]+cand)
    return dp[i][cur_neg_num]

ret=-sys.maxsize
for idx in range(n):
    ret=max(ret, get_min_dis(idx, 0))
print(ret)