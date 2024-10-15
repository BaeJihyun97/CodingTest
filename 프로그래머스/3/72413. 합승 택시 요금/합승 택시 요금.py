import heapq
from collections import deque

MAXV = 100001*200

def dijkstra(n, graph, node):
    que = [(0, node)]
    visited = [False] * (n+1)
    dp = [MAXV] * (n+1)
    
    dp[node] = 0 
    
    while len(que) > 0:
        currw, curr = heapq.heappop(que)
        
        if visited[curr]:
            continue
        
        visited[curr] = True
            
        for nxt, nxtw in graph[curr]:
            nxt_w = currw + nxtw
            if not visited[nxt] and nxt_w < dp[nxt]:
                dp[nxt] = nxt_w
                heapq.heappush(que, (nxt_w, nxt))
                
    return dp

def solution(n, s, a, b, fares):
    answer = 0
    
    # make graph
    graph = [[] for _ in range(n+1)]
    for n1, n2, w in fares:
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    
    a_path = dijkstra(n, graph, a)
    b_path = dijkstra(n, graph, b)
    s_path = dijkstra(n, graph, s)
    
    answer = MAXV
    for i in range(1, n+1):
        new_fare = s_path[i] + a_path[i] + b_path[i]
        if answer > new_fare:
            answer = new_fare

    return answer