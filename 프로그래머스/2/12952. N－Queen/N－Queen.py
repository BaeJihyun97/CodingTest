# def putQeen(n, qi, qj, chess):
#     ci, cj = qi, qj
    
#     for i in range(n):
#         chess[i][qj] = False
    
#     for j in range(n):
#         chess[qi][j] = False
        
#     for 

def isPossible(plusSet, minusSet, ijSet, qi, qj):
    if (qi, qj) in ijSet:
        return False
    if qi+qj in plusSet:
        return False
    if qi-qj in minusSet:
        return False

    return True

def setAdd(plusSet, minusSet, ijSet, qi, qj):
    ijSet.add((qi, qj))
    plusSet.add(qi+qj)
    minusSet.add(qi-qj)
    return

def setRemove(plusSet, minusSet, ijSet, qi, qj):
    ijSet.remove((qi, qj))
    plusSet.remove(qi+qj)
    minusSet.remove(qi-qj)
    return

def DFS(depth, n, notVisitedSet, plusSet, minusSet, ijSet):
    if depth == n:
        return 1
    
    answer = 0
    for index, j in enumerate(notVisitedSet):
        if isPossible(plusSet, minusSet, ijSet, depth, j):
            setAdd(plusSet, minusSet, ijSet, depth, j)
            answer += DFS(depth+1, n, notVisitedSet[:index]+notVisitedSet[index+1:], plusSet, minusSet, ijSet)
            setRemove(plusSet, minusSet, ijSet, depth, j)
            
    return answer

def solution(n):
    answer = 0
    plusSet, minusSet, ijSet = set(), set(), set()
    notVisitedSet = [i for i in range(n)] # 가능한 열

    return DFS( 0, n, notVisitedSet, plusSet, minusSet, ijSet)