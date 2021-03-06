# 그래프 표현 방식에는 인접행렬, 인접리스트 2가지가 있다.
# 공통적으로 각 <인덱스>는 곧 <노드>이다.

###########
##인접행렬: 간선을 행렬형태로 표현하므로, <간선이 0인지 아닌지> 여부로 노드의 연결유무를 파악한다.
###########
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)



#############
##인접리스트: 그냥 노드안에 연결노드와 간선을 함께 넣는다.
#############
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보(노드, 거리)
graph[2].append((0, 5))

print(graph)