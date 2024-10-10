from collections import deque

def switch(i1, j1, i2, j2):
    if i2 < i1 or j2 < j1:
        i1, j1, i2, j2 = i2, j2, i1, j1
    return i1, j1, i2, j2

def move(board, location): # [i1, j1, i2, j2]
    next_location = set()
    i1, j1, i2, j2 = switch(*location)
    # 우, 좌, 하, 상
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i, j in direction:
        i1_, j1_, i2_, j2_ = i1+i, j1+j, i2+i, j2+j
        if board[i1_][j1_] == 0 and board[i2_][j2_] == 0:   
            next_location.add(switch(i1_, j1_, i2_, j2_))
            
    # rotate (i1, j1) 90, -90
    if i1 == i2: # 수평
        if board[i1+1][j1] == 0 and board[i1+1][j1+1] == 0:
            next_location.add(switch(i1, j1, i1+1, j1))
            next_location.add(switch(i1, j1+1, i1+1, j1+1))
        if board[i1-1][j1] == 0 and board[i1-1][j1+1] == 0:
            next_location.add(switch(i1-1, j1, i1, j1))
            next_location.add(switch(i1-1, j1+1, i1, j1+1))
            
    else: # 수직
        if board[i1][j1+1] == 0 and board[i1+1][j1+1] == 0:
            next_location.add(switch(i1, j1, i1, j1+1))
            next_location.add(switch(i1+1, j1, i1+1, j1+1))
        if board[i1][j1-1] == 0 and board[i1+1][j1-1] == 0:
            next_location.add(switch(i1, j1-1, i1, j1))
            next_location.add(switch(i1+1, j1-1, i1+1, j1))
            
    return next_location
    

def solution(board):
    N = len(board)
    answer = 0
    # 주의 범위 1~N 까지 
    board = [[1] * (N+2)] + [[1]+r+[1] for r in board] + [[1] * (N+2)]
    start = (1, 1, 1, 2)
    que = deque([start])
    flag = True
    visited = {(i, j, i+1, j):False for i in range(1, N+1) for j in range(1, N+1)}
    visited.update({(i, j, i, j+1):False for i in range(1, N+1) for j in range(1, N+1)})

    # bfs
    while que and flag:
        temp = set()
        flag = True
        
        while que:
            curr = que.pop()
            if visited[curr]:
                continue
            visited[curr] = True

            if curr[2] == N and curr[3] == N:
                flag = False
                break
            else:
                nextP = move(board, curr)
                for p in nextP:
                    if not visited[p]:
                        temp.add(p)
                        
        if flag:
            answer += 1
            que.clear()
            que.extend(temp)
            temp.clear()
        
    return answer