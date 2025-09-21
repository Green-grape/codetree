n=int(input())

cnt_dict={}
for _ in range(n):
    s=input()
    sorted_s=''.join(sorted(s))
    if sorted_s in cnt_dict:
        cnt_dict[sorted_s]+=1
    else:
        cnt_dict[sorted_s]=1

print(max(list(cnt_dict.values())))
