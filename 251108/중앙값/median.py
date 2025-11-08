from sortedcontainers import SortedList

t = int(input())

for _ in range(t):
    ret = []
    n = int(input())
    pq = SortedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        pq.add(arr[i])
        if i % 2 == 0:
            ret.append(pq[len(pq) // 2])
    print(" ".join(map(str, ret)))
