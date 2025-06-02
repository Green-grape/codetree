str_a=input()
str_b=input()


la=len(str_a)
lb=len(str_b)


dp=[[-1]*(lb+1) for _ in range(la+1)]
dp[0][0]=0

for i in range(la+1):
    for j in range(lb+1):
        if dp[i][j]==-1:
            continue
        if i<la and j<lb and str_a[i]==str_b[j]:
            dp[i+1][j+1]=max(dp[i+1][j+1], 1+dp[i][j])
        
        if i<la:
            dp[i+1][j]=max(dp[i+1][j], dp[i][j])
        if j<lb:
            dp[i][j+1]=max(dp[i][j+1], dp[i][j])

visit=[[False]*(lb+1) for _ in range(la+1)]
moves=[[-1, -1], [-1, 0], [0, -1]]
queue=[(la, lb)]
visit[la][lb]=True

ret=[0]*dp[la][lb]
while len(queue)>0:
    pa, pb=queue.pop(0)
    cur_num=dp[pa][pb]
    for da, db in moves:
        next_a=pa+da
        next_b=pb+db
        if next_a>=0 and next_b>=0 and not visit[next_a][next_b] and 0<=dp[next_a][next_b]<=cur_num:
            if dp[next_a][next_b]<cur_num and next_a<la and ret[cur_num-1]==0:
                ret[cur_num-1]=str_a[next_a]
            visit[next_a][next_b]=True
            queue.append((next_a, next_b))


print(''.join(ret))
            
                
