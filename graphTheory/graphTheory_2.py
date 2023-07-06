# 팀 결성
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

def check_same_team(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        print("YES")
    else:
        print("NO")


n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())

    # 팀 합치기 연산 수행
    if oper == 0:
        union_parent(parent, a, b)

    # 같은 팀 여부 확인 연산 수행
    else:
        check_same_team(parent, a, b)



