# 카드 선택하기 -> dfs + backtracking
# 짝 카드 찾기 -> bfs

from collections import deque

MAXV = 512

# i, j 위치에서 현재 board 상황일때, 조작횟수 1로 움직일 수 있는 방향 반환
def possible(board, i, j):
    rowN, colN = len(board), len(board[0])
    returnList = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 방향키 하나만 조작
    for (di, dj) in directions:
        newi, newj = i+di, j+dj
        if newi >= 0 and newi < rowN and newj >= 0 and newj < colN:
            returnList.add((newi, newj))
            
    # ctrl + 방향키
    for (di, dj) in directions:
        newi, newj = i, j
        while newi+di >= 0 and newi+di < rowN and newj+dj >= 0 and newj+dj < colN:
            newi += di
            newj += dj
            if board[newi][newj] != 0: break
            
        if newi != i or newj != j:
            returnList.add((newi, newj))
            
    return returnList

def findPair(board, r, c, pairNum):
    count, pairP1, pairP2 = 0, [r, c], [-1, -1]    
    rowN, colN = len(board), len(board[0])

    def bfs(pairP, i, j, visited):
        counti = 0
        curr = board[i][j]
        que = deque([(i, j)])
        
        while curr != pairNum and que:
            temp = set()
            counti += 1

            while que:
                (curri, currj) = que.pop()
                if not visited[(curri, currj)]:
                    visited[(curri, currj)] = True
                    nxts = possible(board, curri, currj)

                    for (nxti, nxtj) in nxts:
                        curr = board[nxti][nxtj]
                        if not visited[(nxti, nxtj)]:
                            temp.add((nxti, nxtj))
                        if curr == pairNum:
                            pairP[0] = nxti; pairP[1] = nxtj;
                            break

                if curr == pairNum: break

            que.clear()
            que.extend(temp)
        return counti
    
    # 첫번째 위치 찾기
    visited = {(i, j):False for j in range(colN) for i in range(rowN)}
    count += bfs(pairP1, r, c, visited)
    
    # 두번째 위치 찾기
    board[pairP1[0]][pairP1[1]] = 0
    visited = {(i, j):False for j in range(colN) for i in range(rowN)}
    count += bfs(pairP2, pairP1[0], pairP1[1], visited)
    board[pairP1[0]][pairP1[1]] = pairNum
    
    return count + 2, pairP1, pairP2  
        

def findOrder(board, depth, maxNum, visited, count, i, j):
    if depth == maxNum:
        return count
    
    returnV = MAXV
    for number in range(1, maxNum+1):
        if not visited[number]:
            countN, [p1i, p1j], [p2i, p2j] = findPair(board, i, j, number)
            
            visited[number] = True
            count += countN
            board[p1i][p1j] = 0; board[p2i][p2j] = 0;
            
            returnV = min(returnV, findOrder(board, depth+1, maxNum, visited, count, p2i, p2j))
            
            board[p1i][p1j] = number; board[p2i][p2j] = number;
            count -= countN
            visited[number] = False
            
    return returnV
    

def solution(board, r, c):
    answer = 0
    maxNum = max([max(row) for row in board])
    return findOrder(board, 0, maxNum, [False for _ in range(maxNum+1)], 0, r, c)
