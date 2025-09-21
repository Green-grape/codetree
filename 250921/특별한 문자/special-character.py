s=input()

cnt_dict={}
for c in s:
    if c in cnt_dict:
        cnt_dict[c]+=1
    else:
        cnt_dict[c]=1

ret='None'
ret_idx=len(s)
for k,v in cnt_dict.items():
    if v!=1:
        continue
    cand_idx=s.find(k)
    if cand_idx<ret_idx:
        ret=k
        ret_idx=cand_idx

print(ret)

