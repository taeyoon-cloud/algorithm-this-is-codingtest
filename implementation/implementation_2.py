# 왕실의 나이트
coordinates = input()

x = int(coordinates[1])
y = ord(coordinates[0]) - 96
length = 8 # 체스판 크기

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
count = 0 # 답



for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > length or ny < 1 or ny > length:
        continue
    
    count += 1

print(count)

