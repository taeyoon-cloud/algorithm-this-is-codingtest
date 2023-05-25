n = int(input())
commands = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
command_type = ['L', 'R', 'U', 'D']

x = 0
y = 0
for command in commands:
    i = command_type.index(command)
    
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue

    x = nx
    y = ny

print(x+1, y+1)
