def distance(m, n, startX, startY, targetX, targetY):
    candidate = []
    
    
    if startX < targetX:
        # (0, 0) 모서리
        if targetX / startX  == targetY / startY:
            candidate.append((startX + targetX)**2 + (startY + targetY)**2)
        # (0, n) 모서리
        if targetX / startX == (m-targetY) / (m-startY):
            candidate.append((startX + targetX)**2 + (2*n - startY - targetY)**2)

    elif startX > targetX:
        # (m, n) 모서리
        if (m-targetX) / (m-startX) == (m-targetY) / (m-startY):
            candidate.append((2*m - startX - targetX)**2 + (2*n - startY - targetY)**2)
        # (m, 0) 모서리
        if (m-targetX) / (m-startX) == targetY / startY:
            candidate.append((2*m - startX - targetX)**2 + (startY - targetY)**2)
            
    # x == 0
    if targetY != startY or startX < targetX:
        candidate.append((startX + targetX)**2 + (startY - targetY)**2)
    # x == m
    if targetY != startY or startX > targetX:
        candidate.append((2*m - startX - targetX)**2 + (startY - targetY)**2)
    # y == 0
    if targetX != startX or startY < targetY:
        candidate.append((startX - targetX)**2 + (startY + targetY)**2)
    # y == n
    if targetX != startX or startY > targetY:
        candidate.append((startX - targetX)**2 + (2*n - startY - targetY)**2)
    
    return min(candidate)
        
    

    
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        answer.append(distance(m, n, startX, startY, *ball))
    return answer