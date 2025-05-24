n=int(input())

cache=[0]*(n+1)

MOD=1000000007
def find_kind_square(n):
    if cache[n]!=0:
        return cache[n]
    if n==0:
        cache[n]=1
        return cache[n]
    elif n==1:
        cache[n]=2
        return cache[n]
    iter_list=[i for i in range(n)]
    for num in reversed(iter_list):
        if num!=(n-2):
            cache[n]=(cache[n]%MOD+(2*(find_kind_square(num)))%MOD)%MOD
        else:
            cache[n]=(cache[n]%MOD+(3*(find_kind_square(num)))%MOD)%MOD
    return cache[n]

print(find_kind_square(n))