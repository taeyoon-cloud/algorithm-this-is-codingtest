# 게임 개발
n, m = map(int, input().split()) # n x m 맵
x, y, direction = map(int ,input().split()) # 초기 위치, 초기 방향

arr = [] # 맵 정보를 저장할 2차원 리스트
visited = [[False] * m for _ in range(n)] # 방문하거나 바다인칸은 true, 아니면 false로 초기화할 2차원 리스트
visited[x][y] = True # 초기 위치는 방문 처리

for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

direction_list = ['N', 'E', 'S', 'W'] # 북, 동, 남, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

rotate_count = 0 # 회전 횟수, 4가 되는 순간 break해야 함
answer = 1 # 방문한 총 칸 수

while True:
    # 현재 방향 기준으로 왼쪽으로 90도 회전한 방향부터 탐색
    if direction == 0:
        direction = 3
    else:
        direction -= 1

    rotate_count += 1
    if rotate_count == 4:
        x -= dx[direction]
        y -= dy[direction]
        
        # 뒤로 한칸 가면 그 칸이 바다인 경우 이동하기 전에 멈춤
        if arr[x][y] == 1:
            break
        # 뒤로 한 칸 갈 수 있는 경우 뒤로 한 칸 간 후 멈추므로 answer에 1을 추가하고 멈춤
        else:
            if visited[x][y] == False:
                answer += 1
            break


    nx = x + dx[direction]
    ny = y + dy[direction]

        

    # 맵의 외곽은 항상 바다이므로 맵의 외곽은 갈 수 없다.
    if nx < 1 or nx >= n-1 or ny < 1 or ny >= m-1:
        continue
    if visited[nx][ny] or arr[nx][ny] == 1:
        continue
    else:
        visited[nx][ny] = True
        x = nx
        y = ny
        rotate_count = 0
        answer += 1



print(answer)

    
    