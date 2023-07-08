# 커리큘럼
# 위상 정렬
from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    for x in line[1:-1]:
        graph[x].append(i) # 강의를 들어야 하기 위해 먼저들어야 하는 강의들이 x이므로 x -> i 방향의 간선이 생긴다.
        indegree[i] += 1 # 진입차수 + 1


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    
    print(result[1:])


topology_sort()