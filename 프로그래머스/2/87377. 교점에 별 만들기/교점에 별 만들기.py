from itertools import combinations

def solution(line):
    answer = []
    n = len(line)
    points = []
    
    for line1 in range(n):
        for line2 in range(line1+1, n):
            [A1, B1, C1] = line[line1]
            [A2, B2, C2] = line[line2]
            
            
            y_no, y_deno = A1*C2 - A2*C1, A1*B2 - A2*B1
            if y_deno != 0 and y_no % y_deno == 0:
                y = -y_no // y_deno
                
                if A1 != 0:
                    x_no, x_deno = C1 + B1*y, A1
                else:
                    x_no, x_deno = C2 + B2*y, A2

                if x_deno != 0 and x_no % x_deno == 0:
                    x = -x_no // x_deno
                    points.append((x, y))
                    
    x_list, y_list = [point[0] for point in points], [point[1] for point in points]
    x_max, x_min, y_max, y_min = max(x_list), min(x_list), max(y_list), min(y_list)
    
    
    answer = [["."]*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    points = [(p[0]-x_min, p[1]-y_min) for p in points]
    
    
    max_y = y_max-y_min
    for point in points:
        (i, j) = point
        answer[max_y-j][i] = "*"
        
    answer = ["".join(an) for an in answer]
                    

    return answer