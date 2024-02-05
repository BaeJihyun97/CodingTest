from collections import deque
from copy import deepcopy

def findPosition(maze, curr, ROW, COL, re, be):
    nextRP, nextBP = [], []
    
    # red
    rci, rcj = curr["rpath"][-1]
    
    if re == (rci, rcj):         # endPoint에 먼저 도달했을 경우 현 위치 유지
        nextRP.append((rci, rcj))
    else:                        # endPoint 가 아닐 경우 이동
        if rci + 1 < ROW and maze[rci+1][rcj] != 5 and (rci + 1, rcj) not in curr["rpath"]:
            nextRP.append((rci + 1, rcj))
        if rci - 1 >= 0 and maze[rci-1][rcj] != 5 and (rci - 1, rcj) not in curr["rpath"]:
            nextRP.append((rci - 1, rcj))
        if rcj + 1 < COL and maze[rci][rcj+1] != 5 and (rci, rcj + 1) not in curr["rpath"]:
            nextRP.append((rci, rcj + 1))
        if rcj - 1 >= 0 and maze[rci][rcj-1] != 5 and (rci, rcj - 1) not in curr["rpath"]:
            nextRP.append((rci, rcj - 1))
        
    # blue
    bci, bcj = curr["bpath"][-1]
    
    if be == (bci, bcj):         # endPoint에 먼저 도달했을 경우 현 위치 유지
        nextBP.append((bci, bcj))
    else:                        # endPoint 가 아닐 경우 이동
        if bci + 1 < ROW and maze[bci+1][bcj] != 5 and (bci + 1, bcj) not in curr["bpath"]:
            nextBP.append((bci + 1, bcj))
        if bci - 1 >= 0 and maze[bci-1][bcj] != 5 and (bci - 1, bcj) not in curr["bpath"]:
            nextBP.append((bci - 1, bcj))
        if bcj + 1 < COL and maze[bci][bcj+1] != 5 and (bci, bcj + 1) not in curr["bpath"]:
            nextBP.append((bci, bcj + 1))
        if bcj - 1 >= 0 and maze[bci][bcj-1] != 5 and (bci, bcj - 1) not in curr["bpath"]:
            nextBP.append((bci, bcj - 1))    
        
    return nextRP, nextBP

def findPositionComb(que, curr, nextRP, nextBP, re, be):
    rcurr, bcurr = curr["rpath"][-1], curr["bpath"][-1]
    for rp in nextRP:
        for bp in nextBP:
            if  rp != bcurr or bp != rcurr: # 자리 맞바꾸기 안됨
                if rp == re and bp == be:
                    print("answer:", curr)
                    return max(len(curr["rpath"]), len(curr["bpath"]))
                elif rp != bp:
                    temp = deepcopy(curr)
                    temp["rpath"].append(rp)
                    temp["bpath"].append(bp)
                    que.append(temp)
                
    return -1

def solution(maze):
    answer = 0
    ROW, COL = len(maze), len(maze[0])
    
    # 시작 끝 점 찾기
    rs, bs, re, be = (), (), (), ()
    for i, ma in enumerate(maze):
        for j, m in enumerate(ma):
            if m == 1:
                rs = (i, j)
            elif m == 2:
                bs = (i, j)
            elif m == 3:
                re = (i, j)
            elif m == 4:
                be = (i, j)

    
    # BFS 로 풀어보기. 적어도 16^16 번 안에 찾을 수 있음
    que = deque()
    que.append({"rpath":[rs], "bpath":[bs]})
    
    
    # TODO! 장해물(5) 검사 추가(findPosition)
    # TODO! swap 검사 추가(findPositionComb)
    while len(que) > 0:
        # print(que)
        
        curr = que.popleft()
        nextRP, nextBP = findPosition(maze, curr, ROW, COL, re, be)
        
        flag = findPositionComb(que, curr, nextRP, nextBP, re, be)
        if flag != -1:
            answer = flag
            break

                
    return answer
