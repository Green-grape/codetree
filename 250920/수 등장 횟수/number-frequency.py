n, m=map(int, input().split())
num_list=map(int, input().split())
d={}
for num in num_list:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
target_key_list=map(int, input().split())
print(" ".join([str(d.get(key, 0)) for key in target_key_list]))
