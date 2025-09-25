n=int(input())
n1_set=set(map(int, input().split()))
m=int(input())
m1_list=map(int, input().split())

ret = []
for num in m1_list:
    if num in n1_set: ret.append("1")
    else: ret.append("0")
print("\n".join(ret))

