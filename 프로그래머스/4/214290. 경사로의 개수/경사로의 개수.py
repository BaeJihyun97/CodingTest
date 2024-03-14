from collections import deque
from copy import deepcopy
from numpy import matmul, array, identity, add

def bfs(grid, d, start):
    que = deque([start])
    depth = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    row, col = len(grid), len(grid[0])
    
    for slope in d:
        temp = deque()
        
        while len(que) > 0:
            cur = que.popleft()
            cur_height = grid[cur[0]][cur[1]]
            for dirt in directions:
                i, j = dirt[0] + cur[0], dirt[1] + cur[1]
                if i >= 0 and i < row and j >= 0 and j < col\
                    and grid[i][j] - cur_height == slope:
                    temp.append((i, j, cur[2]))
        
        #[연산줄이기1] 같은 end 면 경우의 수 모아서 다음 기울기(slope) 진행.
        temp_dict = {}
        for (i, j, v) in temp:
            if (i, j) not in temp_dict:
                temp_dict[(i, j)] = v
            else:
                temp_dict[(i, j)] += v
        que = deque([(i, j, v) for (i, j), v in temp_dict.items()])

    
    end_dict = {}
    for (i, j, v) in que:
        if (i, j) not in end_dict.keys():
            end_dict[(i, j)] = v
        else:
            end_dict[(i, j)] += v
            
    return end_dict
        
                    
                    

def findpath(grid, d):
    row, col = len(grid), len(grid[0])
    paths = {}
    
    for i in range(row):
        for j in range(col):
            # 시작점
            start = (i, j, 1)
            possible_path = bfs(grid, d, start)
            
            for key, value in possible_path.items():
                paths[((i, j), key)] = value
    
    # path = {((i1, j1), (i2, j2)) : k, ...} 
    # i, j 는 grid의 좌표값, 1은 시작점, 2는 끝점, k는 시작점에서 끝점으로 가는 경우의 수
    return paths


# 정사각 행렬만 계산
def matrix_product(m1, m2):
    length = len(m1)
    
    m3 = [[0]*length for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            for k in range(length):
                m3[i][j] += m1[i][k] * m2[k][j]
                m3[i][j] %= 1000000007 
                
    return m3

def int2binary(k):
    k_bin = []
    while k > 0:
        k_bin.append(k % 2)
        k //= 2

    return k_bin    

def solution(grid, d, k):
    
    # d 한번 가는 경로 수
    paths = findpath(grid, d)
    
    if len(paths) == 0:
        return 0
    
    # 그래프 만들기
    nodes = {}
    for path, value in paths.items():
        (start, end) = path
        if start not in nodes.keys():
            nodes[start] = len(nodes)
        if end not in nodes.keys():
            nodes[end] = len(nodes)
            
    num_nodes = len(nodes)
    adj_matrix = [[0]*num_nodes for _ in range(num_nodes)]
    for path, value in paths.items():
        (start, end) = path
        start, end = nodes[start], nodes[end]
        adj_matrix[start][end] = value
        
            
    
    # [연산줄이기2] divide & conquer
    # 그냥 for 문 돌리면 시간 초과
    # adj_matrix^(k) 분할 정복
    # k -> int, adj_matrix -> array like
    def mulMatrix(k, adj_matrix):
        if k == 0:
            return adj_matrix
        
        binaryNum = int2binary(k)
        rank = len(adj_matrix)
        
        answer_matrixes = [adj_matrix]
        
        for i in range(1, len(binaryNum)+5):
            prev = answer_matrixes[i-1]
            answer_matrixes.append(matrix_product(prev, prev))

        answer_matrix = [[0]*i + [1] + [0]*(rank-i-1) for i in range(rank)]
        for index, value in enumerate(binaryNum):

            if value == 1:
                answer_matrix = matrix_product(answer_matrix, answer_matrixes[index])

        
        return answer_matrix
    
    # 주의! dtype='int64' 설정 안하면 np 기본 데이터 타입 사용 => 유효 숫자 범위에 따라 오차 발생
    answer_matrix = mulMatrix(k, adj_matrix)
    # answer = answer_matrix.sum() % 1000000007
    # answer = sum([sum(row) % 1000000007 for row in answer_matrix]) % 1000000007
    answer = 0
    for row in answer_matrix:
        for value in row:
            answer += value
            answer %= 1000000007


    return int(answer)



