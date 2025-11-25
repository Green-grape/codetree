from queue import PriorityQueue

n = int(input())

times = []
user_dict = {}
comp_dict = {}


for i in range(n):
    a, b = map(int, input().split())
    times.append((a, 1))
    times.append((b, -1))
    user_dict[a] = i
    comp_dict[b] = a

times.sort()

ret = [0] * n
current_meetings = 0
max_meetings = 0
for time, delta in times:
    current_meetings += delta
    max_meetings = max(max_meetings, current_meetings)

pq = PriorityQueue()
for i in range(1, max_meetings + 1):
    pq.put(i)


for time, delta in times:
    if delta == 1:
        room_number = pq.get()
        user_index = user_dict[time]
        ret[user_index] = room_number
    else:
        start_time = comp_dict[time]
        user_index = user_dict[start_time]
        room_number = ret[user_index]
        pq.put(room_number)

print(" ".join(map(str, ret)))
