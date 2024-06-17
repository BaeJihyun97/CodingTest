# 알고리즘: dfs
# 특징: leaf 노드엔 불이 없어야 함. edge 중 적어도 하나는 불이 있어야함 -> 한번의 순회에 값이 결정됨. O(n)

# 주의! edge 중 적어도 하나 불이 있어야 함. 트리플(node-edge-node) 사이 적어도 하나가 아니라
# 주의! bfs로 풀었을 경우 최상위 레벨의 노들의 토폴로지가 전체 그래프 특징(n노드 n-1엣지)을 가진 여러개의 그래프들. 시간 복잡도 증가

from collections import deque

def dfs(n, graph):
    visited = [False for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]
    lighted = [0 for _ in range(n+1)]
    child_ligted = [[] for _ in range(n+1)]
    stack = deque()
    stack.append(1)
    
    while len(stack) > 0:
        curr = stack[-1]

        if not visited[curr]:
            visited[curr] = True
            is_leaf = True
            
            for nxt in graph[curr]:
                if not visited[nxt]:
                    stack.append(nxt)
                    parent[nxt] = curr
                    is_leaf = False

            if is_leaf:
                lighted[curr] = -1
                child_ligted[parent[curr]].append(-1)
                stack.pop()

        else:
            while len(stack) > 0 and visited[stack[-1]]:
                curr = stack[-1]
                value = 1 if -1 in child_ligted[curr] else -1
                lighted[curr] = value
                child_ligted[parent[curr]].append(value)
                stack.pop()

    return lighted.count(1)
        
    
    
def solution(n, lighthouse):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    # make graph
    for [a, b] in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    # dfs 
    return dfs(n, graph)