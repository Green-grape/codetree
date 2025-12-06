n, m = map(int, input().split())

fires = list(map(int, input().split()))

fire_stations = list(map(int, input().split()))

fires.sort()
fire_stations.sort()

j = 0
max_distance = 0
for i in range(n):
    while j < m - 1 and abs(fires[i] - fire_stations[j]) >= abs(
        fires[i] - fire_stations[j + 1]
    ):
        j += 1
    max_distance = max(max_distance, abs(fires[i] - fire_stations[j]))

print(max_distance)
