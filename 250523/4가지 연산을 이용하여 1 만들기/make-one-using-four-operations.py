n=int(input())

step=[-1]*(2*n+1)

cal_func_list=[
    lambda x: int(x/2) if x%2==0 else x,
    lambda x: int(x/3) if x%3==0 else x,
    lambda x: x-1,
    lambda x: x+1
]

step[n]=0
queue=[(n, 0)]
is_end=False
while len(queue)>0:
    num, cur_cal_cnt=queue.pop(0)
    for cal_func in cal_func_list:
        next_num=cal_func(num)
        if 0<next_num<len(step) and step[next_num]==-1:
            step[next_num]=cur_cal_cnt+1
            if next_num==1:
                is_end=True
                break
            queue.append((next_num, cur_cal_cnt+1))
    if is_end:
        break
        
print(step[1])
