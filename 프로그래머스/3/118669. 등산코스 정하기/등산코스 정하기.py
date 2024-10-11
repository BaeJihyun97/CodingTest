from collections import deque
import heapq

SUMMITTYPE = 1
GATETYPE = 0
MAXWEIGHT =10000001


def solution(n, paths, gates, summits):
    answer = [n+1, MAXWEIGHT]
    graph = [[] for _ in range(n + 1)]

    for n1, n2, w in paths:
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    
    
    dp = [MAXWEIGHT for _ in range(n+1)]
    intensity = 0
    heap = []
    for gate in gates:
        heapq.heappush(heap, (0, gate))
        dp[gate] = 0

    summits_ = set(summits)
    while heap:
        icurr, curr = heapq.heappop(heap)

        if dp[curr] < icurr:
            continue

        for nxt, w in graph[curr]:
            next_intensity = max(icurr, w)
            if next_intensity < dp[nxt]:
                dp[nxt] = next_intensity
                if nxt not in summits_:
                    heapq.heappush(heap, (next_intensity, nxt))

    min_intensity = MAXWEIGHT
    min_summit = n+1
    for summit in summits:
        if dp[summit] < min_intensity:
            min_intensity = dp[summit]
            min_summit = summit
        elif dp[summit] == min_intensity and min_summit > summit:
            min_summit = summit
    
            
    return [min_summit, min_intensity]