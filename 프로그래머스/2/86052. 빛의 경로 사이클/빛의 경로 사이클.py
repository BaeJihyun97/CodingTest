def next_index_direction(grid, position, direction, rowN, colN):
    direction_dic = {0:(1, 0), 1:(-1, 0), 2:(0, 1), 3:(0, -1)}
    direction_dic_L = {0:2, 1:3, 2:1, 3:0}
    direction_dic_R = {0:3, 1:2, 2:0, 3:1}
    
    (i, j) = position
    i = (i + direction_dic[direction][0]) % rowN
    j = (j + direction_dic[direction][1]) % colN
    next_node = grid[i][j]

    if next_node == "S":
        next_direction = direction
    elif next_node == "L":
        next_direction = direction_dic_L[direction]
    else:
        next_direction = direction_dic_R[direction]
        
    return (i, j), next_direction
        
        
        

def visit_cycle(visited, grid, position, direction):
    path = 0
    (i, j) = position
    rowN, colN = len(grid), len(grid[0])
    while not visited[i][j][direction]:
        visited[i][j][direction] = True
        path += 1
        (i, j), direction = next_index_direction(grid, (i, j), direction, rowN, colN)
        
        
    return path

def solution(grid):
    answer = []
    grid2 = []
    rowN, colN, direction = len(grid), len(grid[0]), 4
    direction_dic = {0:(1, 0), 1:(-1, 0), 2:(0, 1), 3:(0, -1)}
    
    for row in grid:
        grid2.append([r for r in row])
        
    visited = [[[False]*4 for _ in range(colN)] for _ in range(rowN)]
        
    
    for i in range(rowN):
        for j in range(colN):
            for d in range(direction):
                if not visited[i][j][d]:
                    
                    path = visit_cycle(visited, grid2, (i, j), d)
                    answer.append(path)
                    
                    
    
    return sorted(answer)