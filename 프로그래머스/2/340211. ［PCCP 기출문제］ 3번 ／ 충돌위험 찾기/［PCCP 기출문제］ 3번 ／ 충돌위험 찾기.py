def get_sign(x):
    return -1 if x < 0 else 1

def check(points):
    lattice = dict()
    crash = 0
    for pL in points:

        p = tuple(pL)
        if p in lattice:
            if lattice[p] == False:
                lattice[p] = True
                crash += 1
        else:
            lattice[p] = False

            
    return crash
                

def solution(points, routes):
    answer = 0
    cache = {}
    paths = []
    
    # 최단 거리 경로 만들기
    for route in routes:
        length = len(route) - 1
        path = [points[route[0]-1]]
        for i in range(length):
            s, e = route[i], route[i+1]
            if (s, e) in cache:
                path += cache[(s, e)]
            else:
                [sr, sc], [er, ec] = points[s-1], points[e-1]
                spath = []
                while sr != er:
                    sr -= get_sign(sr - er)
                    spath.append([sr, sc])
                while sc != ec:
                    sc -= get_sign(sc - ec)
                    spath.append([sr, sc])
                path += spath
                cache[(s, e)] = spath
        paths.append(path)
        
    
    lengths = [len(p) for p in paths]
    maxLen = max(lengths)
    for i in range(maxLen):
        curr_points = []
        for p, length in zip(paths, lengths):
            if i < length:
                curr_points.append(p[i])
        answer += check(curr_points)
                    
    return answer