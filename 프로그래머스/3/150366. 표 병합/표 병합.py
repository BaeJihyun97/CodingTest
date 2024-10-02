from copy import deepcopy
MAX = 16

def update1(table, table_info, r, c, value):
    cells = table_info[(int(r)-1,int(c)-1)]
    for i, j in cells:
        table[i][j] = value
    return

def update2(table, table_info, value1, value2):
    rowL, colL = len(table), len(table[0])
    for i in range(rowL):
        for j in range(colL):
            if table[i][j] == value1:
                table[i][j] = value2
    
def updatef(table, table_info, *args):
    if len(args) >= 3:
        return update1(table, table_info, *args)
    else:
        return update2(table, table_info, *args)
    
def mergef(table, table_info, r1, c1, r2, c2):
    r1, c1, r2, c2 = int(r1)-1, int(c1)-1, int(r2)-1, int(c2)-1
    cells1 = deepcopy(table_info[(r1, c1)])
    cells2 = deepcopy(table_info[(r2, c2)])
    value = table[r1][c1] if table[r1][c1] != "" else table[r2][c2]
    
    for cell1 in cells1:
        table_info[cell1].update(cells2)
    for cell2 in cells2:
        table_info[cell2].update(cells1)
        
    for r, c in cells1 | cells2:
        table[r][c] = value
        
    return

def unmergef(table, table_info, r, c):
    r, c = int(r)-1, int(c)-1
    cells = deepcopy(table_info[(r, c)])
    value = table[r][c]
    
    for cell in cells:
        table_info[cell].clear()
        table_info[cell].add(cell)
        table[cell[0]][cell[1]] = ""
    
    table[r][c] = value
    return

def printf(table, que, r, c):
    r, c = int(r)-1, int(c)-1
    que.append(table[r][c])
    return
    

def solution(commands):
    answer = []
    # table 크기 찾기
    rows, cols = set(), set()
    for command in commands:
        command = command.split(" ")
        if command[0] == "MERGE":
            rows.update([int(command[1]), int(command[3])])
            cols.update([int(command[2]), int(command[4])])
        elif command[0] != "UPDATE" or len(command) != 3:
            rows.add(int(command[1]))
            cols.add(int(command[2]))
    
    maxC, maxR = max(cols), max(rows)

    # 데이터 구조 선언    
    table = [["" for _ in range(maxC)] for _ in range(maxR)] # 값을 저장할 테이블 리스트
    table_info = {(i, j):set([(i, j)]) for i in range(maxR) for j in range(maxC)} # merge 영역을 표시한 딕셔너리
    
    # print(table, table_info)
    # 명령어 수행:
    for command in commands:
        command = command.split(" ")
        c, op = command[0], command[1:]
        if c == "UPDATE":
            updatef(table, table_info, *op)
        elif c == "MERGE":
            mergef(table, table_info, *op)
        elif c == "UNMERGE":
            unmergef(table, table_info, *op)
        else:
            printf(table, answer, *op)
    
    
    return [a if a != "" else "EMPTY" for a in answer ]