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
min3_set = set()
for num in nums:
    pq.put(num)
    if len(pq.elements) < 3:
        ret.append(-1)
        min3_set.add(num)
    else:
        if len(min3_set) == 3 and num <= max(min3_set):
            min3_set.remove(max(min3_set))
            min3_set.add(num)
        elif len(min3_set) < 3:
            min3_set.add(num)
        mult = 1
        for v in min3_set:
            mult *= v
        ret.append(mult)


print("\n".join(map(str, ret)))
