# # N, M을 공백으로 구분하여 입력받기
# # n, m = map(int, input().split())
# n, m = 4, 4


# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0]*m for _ in range(n)]

# # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
# # x, y, direction = map(int, input().split())
# x, y, direction = 1, 1, 0
# d[x][y] = 1  # 현재 좌표 방문 처리

# # 전체 맵 정보를 입력받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# cnt = 0
# turn_time = 0

# while True:
#     if d[(x + dx[direction])][(y + dy[direction])] == 0 and array[(x + dx[direction])][(y + dy[direction])] == 0:
#         x += dx[direction]
#         y += dy[direction]
#         d[x][y] = 1
#         cnt += 1
#         turn_time = 0
#         if direction == 0:
#             direction += 3
#         else:
#             direction -= 1
#         continue
#     else:
#         if direction == 0:
#             direction += 3
#         else:
#             direction -= 1
#         turn_time += 1
    
#     if turn_time == 4: # 원래는 뒤로 한칸 가는거 구현해야됨(귀챠나서..ㅎㅎ)
#         break

# print('cnt:', cnt)


################################################################################################################
################################################# 해답 #########################################################
################################################################################################################


# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는  경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count) 

### 주의! N,M = 6,6이고 x,y,direction이 1,1,0이고, 육지/바다가 아래와 같을 때는
### 1 1 1 1 1 1
### 1 0 0 0 0 1
### 1 1 0 0 1 1
### 1 1 0 1 1 1
### 1 1 0 1 1 1
### 1 1 1 1 1 1
### 육지를 모두 탐색하지 못한다.
### 즉, 이 문제는 완벽한 게임을 만드는 것이 아니라
### 문제의 조건에 따라 구현만 하면 되는 문제이다.