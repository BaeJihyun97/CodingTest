# 알고리즘: 딕스트라 3번(O(VlogE)) 또는 플로이드 워셜(O(V^3)
# 자료구조: heaqque
# 주의: 문제 풀이를 좀더 알고리즘화 시켜서 생각하기
#       s -> i, i -> a, i -> b 의 경로 합 가중치가 최소인것.
#       s -> i, a -> i, b -> i 각각의 최소값 찾기
#       s, a, b 딕스트라 3번 또는 플로이드 워셜
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

def FloydWarshall(n, s, a, b, fares):
    graph = [[MAXV]*(n+1) for _ in range(n+1)]
    
    for n1, n2, w in fares:
        graph[n1][n2] = w
        graph[n2][n1] = w
        
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    
    answer = graph[s][a] + graph[s][b]        
    for i in range(1, n+1):
        new_fare = graph[s][i] + graph[i][a] + graph[i][b]
        if answer > new_fare:
            answer = new_fare
    return answer

def solution(n, s, a, b, fares):
    answer = 0
    
    # dijkstra
#     graph = [[] for _ in range(n+1)]
#     for n1, n2, w in fares:
#         graph[n1].append((n2, w))
#         graph[n2].append((n1, w))
    
#     a_path = dijkstra(n, graph, a)
#     b_path = dijkstra(n, graph, b)
#     s_path = dijkstra(n, graph, s)
    
#     answer = MAXV
#     for i in range(1, n+1):
#         new_fare = s_path[i] + a_path[i] + b_path[i]
#         if answer > new_fare:
#             answer = new_fare

    # floyd-warshall
    answer = FloydWarshall(n, s, a, b, fares)

    return answer