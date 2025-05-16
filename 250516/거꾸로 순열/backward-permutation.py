n=int(input())

output=[]

cur_nums=[]

def permutation():
    if len(cur_nums)==n:
        output.append(" ".join([str(num) for num in cur_nums]))

    for i in range(1, n+1):
        if i not in cur_nums:
            cur_nums.append(i)
            permutation()
            cur_nums.pop()


permutation()
output=reversed(output)
print("\n".join(output))