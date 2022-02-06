N = 5
dirs = ['R', 'R', 'R', 'U', 'D', 'D']
xy = [1, 1]

for dir in dirs:
    print(dir)
    if dir == 'R':
        if 0 < xy[1]+1 and xy[1]+1 <= N:
            xy[1] += 1
    elif dir == 'L':
        if 0 < xy[1]-1 and xy[1]-1 <= N:
            xy[1] -= 1
    elif 0 < xy[0]-1 and dir == 'U':
        if xy[0]-1 <= N:
            xy[0] -= 1
    elif 0 < xy[0]+1 and dir == 'D':
        if xy[0]+1 <= N:
            xy[0] += 1
    print(xy)

    ############################################
    ################## 해설 ####################
    ############################################
    
    # N을 입력받기
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    
    # L, R, U, D에 따른 이동방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    
    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
    
    print(x, y)