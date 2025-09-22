n=int(input())

num_list=map(int, input().split())

idx_dict={}

for i, num in enumerate(num_list):
    if num in idx_dict: continue
    idx_dict[num]=i+1

for k in sorted(idx_dict.keys()):
    print(f'{k} {idx_dict[k]}')