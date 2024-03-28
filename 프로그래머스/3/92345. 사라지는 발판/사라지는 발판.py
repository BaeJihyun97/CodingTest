# DFS + BackTracking


def solution(board, aloc, bloc):
    answer = -1
    row, col = len(board), len(board[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    INFINIT = 512 # row*col 보다 크기만 하면 됨. 넉넉하게 크게 잡기
    
    def DFS(depth):
        
        turn = aloc if depth % 2 == 0 else bloc
        (i, j) = turn
        
        
        if sum([board[i+d[0]][j+d[1]] if i+d[0] >= 0 and i+d[0] < row and j+d[1] >= 0 and j+d[1] < col else 0 for d in directions]) == 0\
           or board[i][j] == 0:
            return INFINIT - depth
        
        return_v = -INFINIT
        
        board[i][j] = 0
        for direction in directions:
            
            turn[0] += direction[0]
            turn[1] += direction[1]

            if turn[0] >= 0 and turn[0] < row and turn[1] >= 0 and turn[1] < col:
                return_v = max(return_v, DFS(depth+1))
            turn[0] -= direction[0]
            turn[1] -= direction[1]
            
        board[i][j] = 1
        

        return -return_v
            
    return INFINIT-abs(DFS(0))