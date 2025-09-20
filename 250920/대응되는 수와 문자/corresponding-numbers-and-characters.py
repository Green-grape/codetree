n, m=map(int, input().split())
str_to_num={}
num_to_str=[-1]
for i in range(n):
    s=input()
    str_to_num[s]=i+1
    num_to_str.append(s)

def is_string(x):
    alphas=[chr(c) for c in range(97, 123)]
    for a in alphas:
        if a in x: return True
    else: return False

for _ in range(m):
    t=input()
    if is_string(t):
        print(str_to_num[t])
    else:
        print(num_to_str[int(t)])
