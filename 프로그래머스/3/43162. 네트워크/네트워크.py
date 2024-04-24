from collections import deque

def bfs(graph, visited, node):
    que = deque()
    que.append(node)
    
    while len(que) > 0:
        curr = que.popleft()
        if not visited[curr]:
            visited[curr] = True
            for nextnode in graph[curr]:
                if not visited[nextnode]:
                    que.append(nextnode)
    
    return


def solution(n, computers):
    answer = 0
    
    # edge list로 만들기
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
                
    visited = [False for _ in range(n)]            
    for node in range(n):
        if not visited[node]:
            answer += 1
            bfs(graph, visited, node)
    
    return answer