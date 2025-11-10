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
        return self.elements[0] if self.elements else None


pq = PriorityQueue()

n = int(input())

nums = list(map(int, input().split()))

ret = []
for num in nums:
    pq.put(num)
    if len(pq.elements) < 3:
        ret.append(-1)
    else:
        first = pq.pop()[0]
        second = pq.pop()[0]
        third = pq.pop()[0]
        ret.append(first * second * third)
        pq.put(first)
        pq.put(second)
        pq.put(third)

print("\n".join(map(str, ret)))
