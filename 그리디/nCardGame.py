n, m = map(int, input().split())    # N, M 입력

result = 0
for _ in range(n):                          # N번 반복 (1행 ~ N행)
    data = list(map(int, input().split()))  # M개의 자연수 입력 받음
    min_value = min(data)                   # 입력받은 것 중 가장 작은 값 찾음
    result = max(result, min_value)         # 이전의 가장 작은 수와 현재의 가장 작은 수 둘 중에 가장 큰 수 찾음

print(result)

######################################################################
##################################답2#################################
#####################################################################

n, m = map(int, input().split())    # N, M 입력

result = 0
for _ in range(n):                          # N번 반복 (1행 ~ N행)
    data = list(map(int, input().split()))  # M개의 자연수 입력 받음
    min_value = 10001                       # 최솟값 설정
    for x in data:                          # 받은 데이터들 각각에 대해
        min_value = min(min_value, x)       # 가장 작은 값 찾기
    result = max(result, min_value)         # 가장 작은 값들 중 가장 큰 값 찾기

print(result)