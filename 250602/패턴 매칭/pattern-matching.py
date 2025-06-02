str_a=input()
pattern=input()

pattern_list=[]
i=len(pattern)-1
while i>=0:
    if pattern[i]!='*':
        pattern_list.insert(0, pattern[i])
        i-=1
    else:
        pattern_list.insert(0, pattern[i-1]+pattern[i])
        i-=2

la=len(str_a)
lp=len(pattern_list)

dp=[[False]*(lp+1) for _ in range(la+1)]
dp[0][0]=True

for i in range(la+1):
    for j in range(lp):
        if dp[i][j]==False:
            continue
        if len(pattern_list[j])==1:
            if i<la and (str_a[i]==pattern_list[j] or pattern_list[j]=='.'):
                dp[i+1][j+1]=dp[i+1][j+1] | dp[i][j]
        else:
            cur_pattern=pattern_list[j][0]
            cur_i=i
            dp[cur_i][j+1]=dp[cur_i][j+1] | dp[i][j]
            while cur_i<la and (str_a[cur_i]==cur_pattern or cur_pattern=='.'):
                dp[cur_i+1][j+1]=dp[cur_i+1][j+1] | dp[i][j]
                cur_i+=1

print('true' if dp[la][lp] else 'false')