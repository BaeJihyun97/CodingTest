from collections import deque

def findIntersection(point1, point2, point3, point4):
    if (point1[0]==point2[0] and point3[0]==point4[0]) or \
       (point1[1]==point2[1] and point3[1]==point4[1]):     # x축 / y축 평행
        return False, ()
    
    x1, x2, y1, y2 = point1, point2, point3, point4
    if point1[0] == point2[0]:
        y1, y2, x1, x2 = point1, point2, point3, point4
        
    x, y, xs, xe, ys, ye = y1[0], x1[1], x1[0], x2[0], y1[1], y2[1]
    if xs > xe: xs, xe = xe, xs
    if ys > ye: ys, ye = ye, ys

    if x > xs and x < xe and y > ys and y < ye:
        return True, (x, y)
    else:
        return False, ()

def check(rec1, rec2):
    points = set()
    cflag = False
    for i in range(4):
        for j in range(4):
            flag, point = findIntersection(rec1[i], rec1[(i+1) % 4], rec2[j], rec2[(j+1) % 4])
            if flag:
                cflag = True
                points.add(point)
                
    return cflag, points

def check2(rectangle, point):
    x, y, x1, x2, y1, y2 = point[0], point[1], rectangle[0][0], rectangle[2][0], rectangle[0][1], rectangle[2][1]
    
    if x > x1 and x < x2 and y > y1 and y < y2:
        return True
    else:
        return False
    
def check2_2(i, graph, rectangles_node_i, x, y):
    for nextRec in graph[i]:
        if check2(rectangles_node_i[nextRec], (x, y)):
            return False
    return True
    
def check3_2(x1, y1, x2, y2, x, y):
    if (x == x1 and y >= y1 and y <= y2) or\
       (x == x2 and y >= y1 and y <= y2) or\
       (y == y1 and x >= x1 and x <= x2) or\
       (y == y2 and x >= x1 and x <= x2):
        return True
    return False

def check3(rectangle, x, y):
    for i, rec in enumerate(rectangle):
        if check3_2(*rec, x, y):
            return i
    return -1

def bfs(rectangle, rectangles_node_i, graph, nodes_dict, characterX, characterY, itemX, itemY):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    currx, curry, currRec = characterX, characterY, check3(rectangle, characterX, characterY)
    que = deque([(currx, curry, currRec)])
    visited = set()
    count = 0
    flag = False
    
    while (currx != itemX or curry != itemY) and count < 800:
        temp = []
        while len(que) > 0:
            (currx, curry, currRec) = que.popleft()
            
            if currx == itemX and curry == itemY:
                flag = True
                break
            
            if (currx, curry) not in visited:
                visited.add((currx, curry))
                
                
                for d in directions:
                    point = (currx + d[0], curry + d[1])
                    canRec = nodes_dict[(currx, curry)] if (currx, curry) in nodes_dict else [currRec]

                    for rec in canRec:
                        if check3_2(*rectangle[rec], currx + d[0]/2, curry + d[1]/2) and \
                           check2_2(rec, graph, rectangles_node_i, currx + d[0]/2, curry + d[1]/2): # 해당 사각형 위/ 다른 사각형 안이 아님.
                            temp.append((*point, rec))
        
        if flag:
            break
        else:
            que.clear()
            que.extend(temp)
            count += 1 
            
    return count


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 사각형 4개의 꼭짓점으로
    rectangles = []
    for r in rectangle:
        rectangles.append(((r[0], r[1]), (r[0], r[3]), (r[2], r[3]), (r[2], r[1]))) # 좌하, 좌상, 우상, 우하 (시계방향: check함수 순서 필수)
    
    # 겹치는 사각형
    nodes = [[] for _ in range(len(rectangle))]
    rectangles_node = {key:i for i, key in enumerate(rectangles)}
    rectangles_node_i = {value: key for key, value in rectangles_node.items()}
    graph = [[] for _ in range(len(rectangles_node))]
    for i, rec in enumerate(rectangles[:-1]):
        for j in range(i+1, len(rectangles)):
            flag, points = check(rectangles[i], rectangles[j])
            if flag:
                graph[rectangles_node[rectangles[i]]].append(rectangles_node[rectangles[j]])
                graph[rectangles_node[rectangles[j]]].append(rectangles_node[rectangles[i]])
                
                for p in points: 
                    nodes[rectangles_node[rectangles[i]]].append((*p, j))
                    nodes[rectangles_node[rectangles[j]]].append((*p, i))

    # node
    nodes_dict = {}
    for rec, i in rectangles_node.items():
        for point in rec:
            flag = True
            for nextRec in graph[i]:
                if check2(rectangles_node_i[nextRec], point):
                    flag = False
                    break
            if flag:
                if point in nodes_dict:
                    nodes_dict[point].add(i)
                else:
                    nodes_dict[point] = set([i])
        
        for (x, y, linkedR) in nodes[i]:
            flag = True
            for nextRec in set(graph[i] + graph[linkedR]):
                if check2(rectangles_node_i[nextRec], (x, y)):
                    flag = False
                    break
            if flag:
                if (x, y) in nodes_dict:
                    nodes_dict[(x, y)].add(i)
                    nodes_dict[(x, y)].add(linkedR)
                else:
                    nodes_dict[(x, y)] = set([i, linkedR])
                
    # character 위치한 사각형
    startRec, endRec = check3(rectangle, characterX, characterY), check3(rectangle, itemX, itemY)
    
    
    answer = bfs(rectangle, rectangles_node_i, graph, nodes_dict, characterX, characterY, itemX, itemY)

    
    return answer