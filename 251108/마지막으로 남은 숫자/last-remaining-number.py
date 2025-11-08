import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def top(self):
        return self.elements[0][1] if self.elements else None


n = int(input())

pq = PriorityQueue()

nums = list(map(int, input().split()))

for num in nums:
    pq.put(num, -num)

while len(pq.elements) > 1:
    first = pq.pop()
    second = pq.pop()
    diff = abs(first - second)
    if diff != 0:
        pq.put(diff, -diff)

if pq.is_empty():
    print(-1)
else:
    print(pq.pop())
