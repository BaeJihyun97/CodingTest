from collections import deque

def nextLocation(board, curri, currj):
    row, col = len(board), len(board[0])
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌, 우, 상, 하
    nextl = []
    
    # for (ho, ve) in direction:
    #     i, j = curri, currj
    #     while i < row-ho and j < col-ve and i >= -ho and j >= -ve and board[i+ho][j+ve] != "D": 
    #         i += ho
    #         j += ve
    #     if i != curri or j != currj: nextl.append((i, j))
    i, j = curri, currj
    while i < row-1 and board[i+1][j] != "D": i += 1
    if i != curri: nextl.append((i, j))
    
    i, j = curri, currj
    while i > 0 and board[i-1][j] != "D": i -= 1
    if i != curri: nextl.append((i, j))
    
    i, j = curri, currj
    while j < col-1 and board[i][j+1] != "D": j += 1
    if j != currj: nextl.append((i, j))
    
    i, j = curri, currj
    while j > 0 and board[i][j-1] != "D": j -= 1
    if j != currj: nextl.append((i, j))
    
    return nextl
    


def solution(board):
    initial, goal = (), ()
    for i, bo in enumerate(board):
        for j, b in enumerate(bo):
            if b == "R":
                initial = (i, j)
            if b == "G":
                goal = (i, j)
                
    
    # BFS 해보기 => timeout
    # VISITED 추가. 다른 path에서 이전 혹은 같은 차수에 방문하는 위치는 다시 방문할 필요 없음.
    que = deque([[initial]]) # 지나왔던 path 저장
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    while len(que) > 0:
        currpath = que.popleft()
        curr = currpath[-1]
        nextl = nextLocation(board, curr[0], curr[1])
        for n in nextl:
            if n == goal:
                return len(currpath)
            if n not in currpath and not visited[n[0]][n[1]]:
                visited[n[0]][n[1]] = True
                que.append([*currpath, n])
    
    return -1