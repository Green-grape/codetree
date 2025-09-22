n=int(input())

cnt_dict={}
for _ in range(n):
    s=input()
    cnt_dict[s]=cnt_dict.get(s, 0)+1

sorted_keys=sorted(cnt_dict.keys())
total_cnt=sum(cnt_dict.values())

for k in sorted_keys:
    print(f'{k} {cnt_dict[k]/total_cnt*100:.4f}')