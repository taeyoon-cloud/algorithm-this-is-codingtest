# 다익스트라 알고리즘 사용
import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[]  for _ in range(n+1)]
distance = [INF] * (n+1)

# 자기 자신에서 자기 자신으로 가는 거리는 0
for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

# 1 -> k -> x 최단 거리
x, k = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.push(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist + q[0]:
            continue
            
        for i in graph[now]:
            # cost = dist + i[0]
            cost = dist + 1
            
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

# 1 -> k까지의 거리를 구하기 위한 dijkstra함수
dijkstra(1)
first = distance[k]

# distance 리스트 초기화
distance = [INF] * (n+1)

# k -> x까지의 거리를 구하기 위한 dijkstra함수
dijkstra(k)
second = distance[x]

# 1 -> k까지의 최단 거리 + k -> x까지의 최단 거리
print(first+second)
