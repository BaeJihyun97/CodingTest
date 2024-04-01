from copy import deepcopy

def rotate90(key):
    row, col = len(key), len(key[0])
    new_key = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(key[row-j-1][i])
        new_key.append(temp)
    return new_key

def check(key, x, y, lock, N, M):
    temp = deepcopy(lock)
    for i in range(M):
        for j in range(M):
            temp[x+i][y+j] += key[i][j]
            
    for i in range(M, N+M):
        for j in range(M, N+M):
            if temp[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N, M = len(lock), len(key)
    lock = [[0]*(N+2*M) for _ in range(M)] + [[0]*M+l+[0]*M for l in lock] + [[0]*(N+2*M) for _ in range(M)]
    keys = [deepcopy(key)]
    
    temp = deepcopy(key)
    for _ in range(3):
        temp = rotate90(temp)
        keys.append(temp)
    
    for key in keys:
        for x in range(1, M+N):
            for y in range(1, M+N):
                if check(key, x, y, lock, N, M):
                    # print(x, y, key)
                    return True
    return False