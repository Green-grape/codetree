n, k=map(int, input().split())
num_list=map(int, input().split())

cnt_dict={}
for num in num_list:
    if num in cnt_dict:
        cnt_dict[num]+=1
    else:
        cnt_dict[num]=1

sorted_keys=sorted(list(cnt_dict.keys()))

ret=0
for key in sorted_keys:
    if key>=k-key:
        break
    if k-key in cnt_dict:
        ret+=cnt_dict[key]*cnt_dict[k-key]

if k%2==0 and (k//2 in cnt_dict):
    ret+=int(cnt_dict[k//2]*(cnt_dict[k//2]-1)/2)
print(ret)
    