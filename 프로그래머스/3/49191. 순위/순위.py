from copy import deepcopy
from numpy import array, matmul, where, count_nonzero

# 정사각 행렬만 계산
def matrix_product(m1, m2):
    length = len(m1)
    
    m3 = [[0]*length for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            for k in range(length):
                m3[i][j] += m1[i][k] * m2[k][j]
                
    return m3 

def solution(n, results):
    answer = 0 
    adj_matrix = array([[0]*n for _ in range(n)], dtype="int64")
    
    for result in results:
        win, los = result[0]-1, result[1]-1
        adj_matrix[win][los] = 1
        # adj_matrix[los][win] = -1
        
    cur_matrix = deepcopy(adj_matrix)
    tot_matrix = deepcopy(adj_matrix)
    while cur_matrix.any():
        cur_matrix = matmul(cur_matrix, adj_matrix)
        tot_matrix = tot_matrix + cur_matrix
    
    
    tot_matrix = tot_matrix + tot_matrix.T
    for row in tot_matrix:
        if count_nonzero(row) == n-1:
            answer += 1
    
    return answer