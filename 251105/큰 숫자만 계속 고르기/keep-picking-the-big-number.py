import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority=None):
        if priority is None:
            priority = -item
        heapq.heappush(self.elements, (priority, item))

    def size(self):
        return len(self.elements)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self.elements)[1]

    def top(self):
        if self.is_empty():
            raise IndexError("top from an empty priority queue")
        return self.elements[0][1]


n, m = map(int, input().split())


pq = PriorityQueue()

nums = list(map(int, input().split()))

for num in nums:
    pq.put(num)


for _ in range(m):
    a = pq.pop()
    a -= 1
    pq.put(a)

print(pq.top())
