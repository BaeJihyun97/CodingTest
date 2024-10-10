from collections import deque
import heapq


def solution(alp, cop, problems):
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    min_alp = max([p[0] for p in problems])
    min_cop = max([p[1] for p in problems])
    MAXCOST = max((min_alp - alp), 0) + max((min_cop - cop), 0)
    MAXREQ = min(max(min_alp, min_cop) * 2, 150)
    dp = dict()

    
    heap = []
    cost = 0
    heapq.heappush(heap, (cost, (alp, cop)))
    dp[(alp, cop)] = cost
    
    while heap[0][1][0] < min_alp or heap[0][1][1] < min_cop:
        cost, (alp, cop)  = heapq.heappop(heap)
        
        for p0, p1, p2, p3, p4 in problems:
            if p0 <= alp and p1 <= cop:
                nalp, ncop, ncost = min(alp+p2, MAXREQ), min(cop+p3, MAXREQ), cost+p4
                key = (nalp, ncop)
                if key not in dp or dp[key] > ncost:
                    heapq.heappush(heap, (ncost, key))
                    dp[key] = ncost
                    # print("curr", (alp, cop, cost,), "new", (nalp, ncop, ncost), "cost", dp[(nalp, ncop)])
    
    return heap[0][0]