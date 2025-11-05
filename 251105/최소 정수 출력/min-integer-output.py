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


n = int(input())

pq = PriorityQueue()

ret = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if pq.is_empty():
            ret.append(0)
        else:
            ret.append(pq.pop())
    else:
        pq.put(num, num)
print("\n".join(map(str, ret)))
 