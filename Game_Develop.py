# N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
n, m = 4, 4


# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
x, y, direction = 1, 1, 0
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
turn_time = 0

while True:
    if d[(x + dx[direction])][(y + dy[direction])] == 0 and array[(x + dx[direction])][(y + dy[direction])] == 0:
        x += dx[direction]
        y += dy[direction]
        d[x][y] = 1
        cnt += 1
        turn_time = 0
        if direction == 0:
            direction += 3
        else:
            direction -= 1
        continue
    else:
        if direction == 0:
            direction += 3
        else:
            direction -= 1
        turn_time += 1
    
    if turn_time == 4:
        break

print('cnt:', cnt)
