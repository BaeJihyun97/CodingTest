from collections import deque

MAXV = 1000001

def solution(x, y, n):
    array = [-1]*MAXV
    minV = x
    que = deque()
    que.append(x)
    index = 1
    answer = -1
    array[x] = 0 
    
    
    while minV < y and array[y] == -1:
        que2 = deque()
        minV2 = []
        while que:
            curr = que.pop()
            if curr+n < MAXV and array[curr+n] == -1:
                que2.append(curr+n)
                array[curr+n] = index
            if curr*2 < MAXV and array[curr*2] == -1:
                que2.append(curr*2)
                array[curr*2] = index
            if curr*3 < MAXV and array[curr*3] == -1:
                que2.append(curr*3)
                array[curr*3] = index
            
            minV2.append(min([curr+n, curr*2, curr*3]))
            
        minV = min(minV2)

        index += 1
        que = que2

    
    if array[y] != -1:
        answer = array[y]
        
        
    return answer