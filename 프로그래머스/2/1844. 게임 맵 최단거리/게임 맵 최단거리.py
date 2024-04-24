from collections import deque

def bfs(maps):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque()
    que.append((1, 1))
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    n, m = len(maps)-2, len(maps[0])-2
    maxCount = n*m
    flag = False
    
    while count < maxCount:
        temp = []
        count += 1
        while len(que) > 0:
            (curri, currj) = que.popleft()
            if curri == n and currj == m:
                flag = True
                break
            elif not visited[curri][currj]:
                visited[curri][currj] = True

                for d in directions:
                    nexti, nextj = curri+d[0], currj+d[1]
                    if not visited[nexti][nextj] and maps[nexti][nextj] == 1:
                        temp.append((nexti, nextj))

        if flag:
            break
        else:
            que.clear()
            que.extend(temp)
            
    if flag: return count
    else: return -1
    


def solution(maps):
    answer = 0
    length = len(maps[0])
    maps = [[0]*(length+2)] + [[0]+m+[0] for m in maps] + [[0]*(length+2)]
    
    
    return bfs(maps)