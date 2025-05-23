n=int(input())

MAX_N=45
cache=[0]*(MAX_N+1)
def get_fibo_num(n):
    if cache[n]!=0:
        return cache[n]
    if n<=2:
        return 1
    cache[n]=get_fibo_num(n-1)+get_fibo_num(n-2)
    return cache[n]

print(get_fibo_num(n))
