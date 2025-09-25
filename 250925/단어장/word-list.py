n=int(input())

cnt_dict={}

for _ in range(n):
    s=input()
    cnt_dict[s]=cnt_dict.get(s, 0)+1


sorted_keys=sorted(cnt_dict.keys())

ret=""
for key in sorted_keys:
    ret+=f"{key} {cnt_dict[key]}\n"

print(ret)