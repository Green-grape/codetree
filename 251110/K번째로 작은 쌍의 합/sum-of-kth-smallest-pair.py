n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, *item):
        heapq.heappush(self.elements, item)

    def pop(self):
        return heapq.heappop(self.elements)

    def top(self):
        return self.elements[0][1] if self.elements else None


pq = PriorityQueue()

for i in range(n):
    pq.put(a[i] + b[0], a[i], b[0], 0)


ret = 0
while k > 0:
    val, x, y, idx = pq.pop()
    ret = val
    k -= 1
    if idx + 1 < m:
        pq.put(x + b[idx + 1], x, b[idx + 1], idx + 1)
print(ret)
