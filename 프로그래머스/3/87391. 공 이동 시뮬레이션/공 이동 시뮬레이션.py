def move(end_points, query, n, m):
    [mode, count] = query
    r1p, r1c, r2p, r2c, c1p, c1c, c2p, c2c = end_points
    
    def moveI(startP_, endP_, startP, endP, maxV, remainC, moveC):
        if startP_ == endP_:
            return maxV, maxV
        elif startP_ == endP_ + 1:
            return remainC - moveC, moveC
        else:
            return remainC + ((endP - startP) - (endP_ - startP_)), moveC
        
    
    if mode == 0:
        startP_, endP_ = max(0, c1p - count), max(0, c2p - count)
        
        c1c, c2c = moveI(startP_, endP_, c1p, c2p, m, c1c, c2c)
        c1p, c2p = startP_, endP_
        
    elif mode == 1:
        startP_, endP_ = min(m-1, c1p + count), min(m-1, c2p + count)
        
        c2c, c1c = moveI(startP_, endP_, c1p, c2p, m, c2c, c1c)
        c1p, c2p = startP_, endP_

    elif mode == 2: 
        startP_, endP_ = max(0, r1p - count), max(0, r2p - count)
        
        r1c, r2c = moveI(startP_, endP_, r1p, r2p, n, r1c, r2c)
        r1p, r2p = startP_, endP_
                
    else:
        startP_, endP_ = min(n-1, r1p + count), min(n-1, r2p + count)
        
        r2c, r1c = moveI(startP_, endP_, r1p, r2p, n, r2c, r1c)
        r1p, r2p = startP_, endP_
    
    # print(query, ":", r1p, r1c, r2p, r2c, c1p, c1c, c2p, c2c)
    return [r1p, r1c, r2p, r2c, c1p, c1c, c2p, c2c]
        

        
            
def solution(n, m, x, y, queries):
    end_points = [0, 1, n-1, 1, 0, 1, m-1, 1]
    
    for query in queries:
        end_points = move(end_points, query, n, m)
    
    # print(end_points)
    r1p, r1c, r2p, r2c, c1p, c1c, c2p, c2c = end_points
    answer = 1
    if x == r1p:
        answer *= r1c
    elif x == r2p:
        answer *= r2c
    elif x < r1p or x > r2p:
        answer = 0
        
    if y == c1p:
        answer *= c1c
    elif y == c2p:
        answer *= c2c
    elif y < c1p or y > c2p:
        answer = 0
    
    return answer