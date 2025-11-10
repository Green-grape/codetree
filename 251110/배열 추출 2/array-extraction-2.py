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

n = int(input())

ret = []
for _ in range(n):
    num = int(input())
    if num == 0:
        ret.append(pq.pop()[1] if not pq.is_empty() else 0)
    else:
        pq.put(abs(num), num)
print("\n".join(map(str, ret)))
