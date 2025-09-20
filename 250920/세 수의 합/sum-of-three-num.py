n, target=map(int, input().split())

num_list=map(int, input().split())

cnt_dict={}
for num in num_list:
    if num in cnt_dict:
        cnt_dict[num]+=1
    else:
        cnt_dict[num]=1

sorted_keys=sorted(list(cnt_dict.keys()))

ret=0
# 3개의 숫자가 모두 다른 경우
for i in range(len(sorted_keys)):
    for j in range(i+1, len(sorted_keys)):
        remain_num=target-sorted_keys[i]-sorted_keys[j]
        if not remain_num>sorted_keys[j]: continue
        ret+=cnt_dict[sorted_keys[i]]*cnt_dict[sorted_keys[j]]*cnt_dict.get(remain_num, 0)

# 2개의 숫자가 같은 경우
for i in range(len(sorted_keys)):
    for j in range(i+1, len(sorted_keys)):
        if sorted_keys[i]*2+sorted_keys[j]==target:
            c_i=cnt_dict[sorted_keys[i]]
            c_j=cnt_dict[sorted_keys[j]]
            ret+=int((c_i-1)*c_i/2*c_j)
        elif sorted_keys[i]+sorted_keys[j]*2==target:
            c_i=cnt_dict[sorted_keys[i]]
            c_j=cnt_dict[sorted_keys[j]]
            ret+=int((c_j-1)*c_j/2*c_i)

# 3개의 숫자가 같은경우
if target%3==0 and (target//3 in cnt_dict):
    c_t3=cnt_dict[target//3]
    ret+=int(c_t3*(c_t3-1)*(c_t3-2)/6)

print(ret)

