# 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)] # 방문 여부 확인

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1 # 방문한 칸 개수

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True # 초기 위치는 방문 처리

    while queue:
        x, y = queue.popleft() 
        
        # 현재 위치에서 상, 하, 좌, 우 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 맵 안에 있어야지만 방문 가능하다.
                if graph[nx][ny] == 0: # 괴물이 있는 경우 방문할 수 없다.
                    continue
                if not visited[nx][ny]: # 맵 안에 있고, 방문 가능한 칸의 경우
                    graph[nx][ny] = graph[x][y] + 1 # 이전 칸에다가 + 1
                    queue.append((nx, ny)) # 큐에 추가
                    visited[nx][ny] = True

    return graph[n-1][m-1] # 마지막 칸 리턴

print(bfs(0, 0))
    