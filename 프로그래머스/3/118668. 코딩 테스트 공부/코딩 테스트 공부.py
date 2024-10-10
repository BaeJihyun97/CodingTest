# 알고리즘: 다익스트라
# 자료구조: heapq

import heapq

# MAXREQ 가 150 이하가 맞을까? 
# O 정확한 path를 구하는 것이 아님 -> 즉  min_alp, min_cop 만 넘기면 그 이상의 값은 구분할 필요 없음.
def solution(alp, cop, problems):
    # 1. 초기화
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]  # 엣지(그래프 역할)
    min_alp = max([p[0] for p in problems])         # 요구되는 alp의 최솟값
    min_cop = max([p[1] for p in problems])         # 요구되는 cop의 최솟값
    MAXCOST = max((min_alp - alp), 0) + max((min_cop - cop), 0) # 최대 비용. 문제X 공부로만
    dp = [[MAXCOST]*(min_cop+1) for _ in range(min_alp+1)]      # 최소 비용(최단 거리) 리스트
    visited = [[False]*(min_cop+1) for _ in range(min_alp+1)]   # 방문 여부 리스트
    heap = []   # working que
    
    # 출발 노드 넣기
    alp, cop = min(alp, min_alp), min(cop, min_cop) # 주의! maximum 값 제한
    cost = 0
    heapq.heappush(heap, (cost, (alp, cop)))
    dp[alp][cop] = cost

    # 4. 조건이 충족될 때까지 반복
    while len(heap) > 0 and (heap[0][1][0] < min_alp or heap[0][1][1] < min_cop):
        cost, (alp, cop)  = heapq.heappop(heap) # 2. 값이 가장 작은 노드 고르기
        
        if visited[alp][cop]:
            continue
        
        visited[alp][cop] = True

        # 3. 최소 비용 리스트 업데이트
        for p0, p1, p2, p3, p4 in problems:
            if p0 <= alp and p1 <= cop:
                nalp, ncop, ncost = min(alp+p2, min_alp), min(cop+p3, min_cop), cost+p4 # 주의! maximum 값 제한

                if  dp[nalp][ncop] > ncost:
                    heapq.heappush(heap, (ncost, (nalp, ncop)))
                    dp[nalp][ncop] = ncost
    
    return heap[0][0] if len(heap) > 0 else MAXCOST


# (alp1, cop1, cost1), (alp2, cop2, cost2) 라면
# cost1 >= cost2 && alp1 <= alp2 && cop1 <= cop2 라면 (alp1, cop1, cost1) 는 더이상 고려하지 않아도 괜찮지 않을까?
# 위 조건 탐색 시간이 dp로 걸려지는 것 보다 더 길듯...