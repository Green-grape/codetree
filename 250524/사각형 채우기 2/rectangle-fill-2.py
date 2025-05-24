n=int(input())

MOD=10007
cache=[0]*(n+1)
def find_rectangle_cnt(n):
    if cache[n]!=0:
        return cache[n]
    if n==1:
        return 1
    elif n==2:
        return 3
    cache[n]=(find_rectangle_cnt(n-1)%MOD+(2*find_rectangle_cnt(n-2))%MOD)%MOD
    return cache[n]

print(find_rectangle_cnt(n))