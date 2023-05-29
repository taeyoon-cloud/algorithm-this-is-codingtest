# 음료수 얼려 먹기
n, m = map(int, input().split()) # 세로 길이 n, 가로 길이 m
graph = [] # 얼음틀
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 1 # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0: # 만약 방문하지 않았다면, 
                dfs(nx, ny) # 해당 칸부터 dfs

# 만들 수 있는 아이스크림 개수
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 방문하지 않은 칸인 경우 그 칸부터 dfs 시작
            dfs(i, j)
            count += 1 # 해당 칸에서의 dfs가 끝나면 count + 1

print(count)