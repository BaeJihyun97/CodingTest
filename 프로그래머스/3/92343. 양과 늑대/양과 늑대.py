# 알고리즘: dfs/bfs
# 자료구조: set (+bitmasking)
# 주의: dfs/bfs 에서 방문할 노드를 문제 그대로의 노드가 아닌, 특정 '상태'로 풀 수도 있음!
#       예를 들면, 0, 1, 2, ... 노드를 탐색하는 것이 아닌, {0}, {0, 1}, {0, 1, 8}, {0, 1, 2}, {0, 1, 4}, ... 로 방문한 노드의 상태를 탐색할 수 있음
#       {0, 1, 8}을 set으로 할수도 있지만(frozenset과 함께), 노드 수가 17보다 같거나 작으니 00000000100000011 으로도 표현 가능! 

import heapq

def DFS(curr, tree, info, nxtnodes, stateSet, sheep, wolf, depth):
    if len(nxtnodes) == 0:
        return sheep
    
    maxSheep = sheep
    for i, nxt in enumerate(nxtnodes):
        nxtset = curr.copy()
        nxtset.add(nxt)
        nxtsheep, nxtwolf = sheep, wolf
        if info[nxt] == 0:
            nxtsheep += 1
        else: 
            nxtwolf += 1

        if frozenset(nxtset) not in stateSet and nxtsheep > nxtwolf:
            stateSet.add(frozenset(nxtset))
            maxSheep = max(maxSheep, DFS(nxtset, tree, info, nxtnodes[:i]+nxtnodes[i+1:]+tree[nxt][1], stateSet, nxtsheep, nxtwolf, depth+1))
            
    return maxSheep
    


def solution(info, edges):
    answer = 0
    
    # make tree
    node = len(info)
    tree = [[-1, []] for _ in range(node)]
    for p, c in edges:
        tree[p][1].append(c)
        tree[c][0] = p

    answer = DFS(set(), tree, info, [0], set(), 0, 0, 0)
    return answer
        
        
    
    