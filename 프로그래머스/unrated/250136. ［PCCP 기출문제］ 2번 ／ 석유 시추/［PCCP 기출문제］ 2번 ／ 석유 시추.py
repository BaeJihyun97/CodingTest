def find_group(i, j, land, visited):
    row_n, col_n  = len(land), len(land[0])
    min_col, max_col = j, j
    stack = [(i, j)]
    count = 0
    
    while len(stack) > 0:
        (i, j) = stack.pop()
        if visited[i][j] == False:
            visited[i][j] = True
            count += 1

            if i - 1 >= 0 and land[i-1][j] == 1 and visited[i-1][j] == False:
                stack.append((i-1, j))
                
            if i + 1 < row_n and land[i+1][j] == 1 and visited[i+1][j] == False:
                stack.append((i+1, j))
                
            if j - 1 >= 0 and land[i][j-1] == 1 and visited[i][j-1] == False:
                stack.append((i, j-1))
                if min_col > j - 1: min_col = j - 1
                
            if j + 1 < col_n and land[i][j+1] == 1 and visited[i][j+1] == False:
                stack.append((i, j+1))
                if max_col < j + 1: max_col = j + 1
            
    return {"amount":count, "min_col":min_col, "max_col":max_col}
            
    
            
    

def solution(land):
    row_n, col_n  = len(land), len(land[0])
    visited = [[False]*col_n for _ in range(row_n)]
    groups = []
    
    # 그룹 묶기 (O(N*M))
    for i in range(row_n):
        for j in range(col_n):
            if land[i][j] == 1 and visited[i][j] == False:
                groups.append(find_group(i, j, land, visited))
            else:
                visited[i][j] = True
                
    # 각 열마다 최대값 계산
    answers = [0] * col_n
    for group in groups:
        for j in range(group["min_col"], group["max_col"]+1):
            answers[j] += group["amount"]
                
    answer = max(answers)

    return answer