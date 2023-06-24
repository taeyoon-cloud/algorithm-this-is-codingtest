# 플로이드-워셜 알고리즘 코드
INF = int(1e9) # 10억(무한을 의미)

n, m = map(int, input().split()) # 노드 개수 n, 간선 개수 m

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트를 만들고 INF로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아 graph의 값을 그 값으로 초기화

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

