possiable_part = {
    (2, 3) : [[[1, 0, 0], [1, 1, 1]], [[0, 0, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1]]],
    (3, 2) : [[[1, 0], [1, 0], [1, 1]], [[0, 1], [0, 1], [1, 1]]]
}

def find_part(board, i, j, number, visited, positions):
    direction = [(1, 0), (0, -1), (0, 1)] # down, left, right
    if i < positions[0]: positions[0] = i
    elif i > positions[1]: positions[1] = i
    if j < positions[2]: positions[2] = j
    elif j > positions[3]: positions[3] = j
        
    
    for di, dj in direction:
        di, dj = i+di, j+dj
        
        if board[di][dj] == number and not visited[di][dj]:
            visited[di][dj] = True
            find_part(board, di, dj, number, visited, positions)

def check(board, number, positions): # case = #row - #col
    imin, imax, jmin, jmax = positions
    block = [[1 if board[i][j] == number else board[i][j]  for j in range(jmin, jmax+1) ] for i in range(imin, imax+1)]
    case = imax-imin-(jmax-jmin)
    
    ns = set([v for row in block for v in row])
    if ns == set([0, 1]):
        if case > 0:
            if block[-1] == [1, 1]:
                j_index = jmin if block[0][0] == 0 else jmax
                for i in range(0, imax):
                    if board[i][j_index] != 0:
                        return False
                return True
        else:
            if block[-1] == [1, 1, 1]:
                j_indexs=[]
                for j in range(jmin, jmax+1): 
                    if board[imin][j] == 0: j_indexs.append(j)
                for j_index in j_indexs:
                    for i in range(0, imax):
                        if board[i][j_index] != 0:
                            return False
                return True
            
    return False   

# def printboard(board):
#     for r in board:
#         print(r)
     

def solution(board):
    answer = 0
    blocks = dict()
    N = len(board)
    board = [[0] * (N+2)] + [[0]+r+[0] for r in board] + [[0] * (N+2)]
    visited = [[False] * (N+2) for _ in range((N+2))]
    
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            number = board[i][j] 
            if number != 0 and not visited[i][j]:
                positions = [i, i, j, j]
                find_part(board, i, j, number, visited, positions)
                blocks[number] = positions
                           
    while True:
        removed = []
        for number, positions in blocks.items():
            imin, imax, jmin, jmax = positions
            if check(board, number, positions):
                answer += 1
                removed.append(number)
                # 지우기
                for i in range(imin, imax+1):
                    for j in range(jmin, jmax+1):
                        board[i][j] = 0
        
        for key in removed:
            blocks.pop(key)
            
        if len(removed) == 0:
            break

            
    
    return answer