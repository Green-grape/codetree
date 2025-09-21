n, m=map(int, input().split())

num_list=map(int, input().split())
cnt_dict={}
for num in num_list:
    if num in cnt_dict:
        cnt_dict[num]=(cnt_dict[num][0]+1, num)
    else:
        cnt_dict[num]=(1, num)

sorted_value=sorted(list(cnt_dict.values()), reverse=True)

ret=" ".join([str(sorted_value[i][1]) for i in range(m)])
print(ret)