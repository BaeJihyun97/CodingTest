from collections import deque

def bfs(table, visited, i, j):
    piece = []
    que = deque([(i, j)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while len(que) > 0:
        (curri, currj) = que.popleft()
        
        if not visited[curri][currj]:
            visited[curri][currj] = True
            piece.append((curri, currj))
            
            for d in directions:
                nexti, nextj = curri + d[0], currj + d[1]
                if table[nexti][nextj] == 1 and not visited[nexti][nextj]:
                    que.append((nexti, nextj))
                    
    # index 배열을 matrix로 바꾸기
    ilist, jlist = [p[0] for p in piece], [p[1] for p in piece]
    imax, imin, jmax, jmin = max(ilist), min(ilist), max(jlist), min(jlist)
    piece_matrix = [[0]*(jmax-jmin+1) for _ in range(imax-imin+1)]
    
    for (i, j) in piece:
        piece_matrix[i-imin][j-jmin] = 1
                    
    return piece_matrix

def rotate90(matrix):
    row, col = len(matrix), len(matrix[0])
    matrix_new = [[0]*row for _ in range(col)]
    
    for i in range(col):
        for j in range(row):
            matrix_new[i][j] = matrix[j][col-i-1]
            
    return matrix_new

def check(board, piece):
    curr = piece
    
    for _ in range(4):
        rowb, colb = len(board), len(board[0])
        rowp, colp = len(curr), len(curr[0])
        flag = False
        if rowb == rowp and colb == colp:
            for i in range(rowb):
                for j in range(colb):
                    if board[i][j] != curr[i][j]:
                        flag = True
                        break
                if flag: break
            
            if not flag:
                return True

        curr = rotate90(curr)
    return False

def solution(game_board, table):
    answer = 0
    N = len(table)
    game_board_r = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                game_board_r[i][j] = 1
                
    
    
    table = [[0]*(N+2)] + [[0]+t+[0] for t in table ] + [[0]*(N+2)]
    game_board_r = [[0]*(N+2)] + [[0]+t+[0] for t in game_board_r ] + [[0]*(N+2)]
    pieces = []
    boards = []

    # table 조각으로 나누기: BFS
    visited = [[False]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if table[i][j] == 1 and not visited[i][j]:
                pieces.append(bfs(table, visited, i, j))
                
    # game_board 조각으로 나누기: BFS
    visited = [[False]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if game_board_r[i][j] == 1 and not visited[i][j]:
                boards.append(bfs(game_board_r, visited, i, j))


    # game_board에 나눠진 조각을 채워넣기
    used = [False] * len(pieces)
    for board in boards:
        for index, piece in enumerate(pieces):
            if not used[index] and check(board, piece):
                used[index] = True
                answer += sum([sum(p) for p in piece])
                break

    return answer