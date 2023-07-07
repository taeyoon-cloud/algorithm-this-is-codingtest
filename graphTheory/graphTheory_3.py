# 도시 분할 계획
# 크루스칼 알고리즘 사용


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 개수 n, 길의 개수 m
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    # 자기 자신의 부모로 초기화
    parent[i] = i

# 간선 정보를 입력받기 위한 edges
edges = []

# 간선 입력
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# cost가 가장 적은 간선부터 시작
edges.sort()

# 연결된 간선 중 가장 cost가 큰 간선의 cost를 저장하기 위한 변수 -> 마지막에 cost 총합에서 빼주면 됨
temp = 0
# 길의 유지비 합의 최솟값 result
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result  += cost
        temp = max(temp, cost)
    
print(result - temp)
