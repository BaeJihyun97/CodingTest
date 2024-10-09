# 자료구조 문제
# 양 끝에서만 값이 바뀜 -> deque
from collections import deque


def Rotate(left, right, middle):
    middle[0].appendleft(left.popleft())
    right.appendleft(middle[0].pop())
    middle[-1].append(right.pop())
    left.append(middle[-1].popleft())
    
def ShiftRow(left, right, middle):
    left.appendleft(left.pop())
    right.appendleft(right.pop())
    middle.appendleft(middle.pop())

def solution(rc, operations):
    rownum, colnum = len(rc), len(rc[0])
    left = deque([rc[i][0] for i in range(rownum)])
    right = deque([rc[i][colnum-1] for i in range(rownum)])
    middle = deque([deque(rc[i][1:colnum-1]) for i in range(rownum)])
    length = 2*(rownum + colnum) - 4
    
    # operations 축약하기
    operations2 = []
    prev, count = operations[0], 0
    for op in operations:
        if op == prev:
            count += 1
        else:
            operations2.append([prev, count])
            prev, count = op, 1
    operations2.append([prev, count])        
    
    
    for op, count in operations2:
        if op == "ShiftRow":
            count %= rownum
            for _ in range(count): ShiftRow(left, right, middle)
        else:
            count %= length
            for _ in range(count): Rotate(left, right, middle)

    answer = [[left.popleft()] + [*middle.popleft()] + [right.popleft()] for _ in range(rownum)]
    return answer



# Rotate 에서 2*(rownum + colnum) - 4 횟수만큼 데이터를 바꿔야 함
# 최악의 경우 rotate, shift 가 반복할 경우 100,000  * 1200 의 메모리 연산
#  Rotate,ShiftRow 각각 하는 것의 최고 효율을 뽑아야함.
# def ShiftRow(rc, count, rownum):
#     count %= rownum
#     return rc[rownum-count:] + rc[:rownum-count]

# def Rotate(rc, count, rownum, colnum):
#     length = 2*(rownum + colnum) - 4
#     count %= length
#     outer = [rc[0][i] for i in range(0, colnum, 1)] + [rc[i][colnum-1] for i in range(1, rownum, 1)] + \
#             [rc[rownum-1][i] for i in range(colnum-2, -1, -1)] + [rc[i][0] for i in range(rownum-2, 0, -1)]
#     outer = outer[length-count:] + outer[:length-count]
#     j = 0
    
#     temp = colnum+rownum+colnum
#     rc[0] = outer[0:colnum]; rc[rownum-1] = outer[temp-3:colnum+rownum-3:-1]
#     for i in range(1, rownum, 1): rc[i][colnum-1] = outer[colnum+i-1]
#     for i in range(2, rownum, 1): rc[rownum-i][0] = outer[temp+i-4]
#     return