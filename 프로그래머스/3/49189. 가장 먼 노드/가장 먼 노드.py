from collections import deque

def solution(n, edge):
    answer = 0
    
    # graph 만들기
    edge_list = [[] for _ in range(n+1)]
    for (n1, n2) in edge:
        edge_list[n1].append(n2)
        edge_list[n2].append(n1)
        
    # BFS
    count = 0
    visited = [-1] * (n+1)
    que = deque([1])
    
    visited[1] = 0
    
    while len(que):
        curr = que.popleft()
        next_nodes = edge_list[curr]
        curr_step = visited[curr]

        for node in next_nodes:
            if visited[node] == -1:
                que.append(node)
                visited[node] = curr_step+1
                
    
    max_v = max(visited)
    for v in visited:
        if v == max_v:
            answer += 1
    
    return answer


