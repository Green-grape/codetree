from sortedcontainers import SortedSet

n, k=map(int, input().split())
num_list=list(map(int, input().split()))

s=SortedSet(num_list, key=lambda x:-x)
print(" ".join(map(str, list(s[:k]))))