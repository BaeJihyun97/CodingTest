from numpy import array, concatenate
from math import log, ceil

def find_count(n, l, r, count_dict):
    if n == 1:       
        temp = [0, 1, 2, 2, 3, 4]
        count_dict[0] += temp[r] - temp [l-1]
        return 
    
    length = 5**(n-1)
    
    # length 단위로 l 보다 큰 가장 작은 수 찾기
    # length 단위로 r 보다 작은 가장 큰 수 찾기
    lN, prevN, rN = 0, 0, length*4
    while lN < l:
        prevN = lN
        lN += length
        
        
    while rN >= r:
        rN -= length

    
    # 위에서 찾은 두 범위가 겹치지 않을 때
    if lN <= rN:
        if not (length*2+1 <= l and length*3 >= lN):
            find_count(n-1, l-prevN, length, count_dict)
        if not (length*2+1 <= rN+1 and length*3 >= r):
            find_count(n-1, 1, r-rN, count_dict)
        temp = (rN-lN)//length
        if length*2+1 >= lN and length*3 <= rN: temp -= 1
        count_dict[n-1] += temp
    # 위에서 찾은 두 범위가 겹칠 때. 즉 r-l 길이가 length 보다 작을 때
    else:
        if not (length*2+1 <= l and length*3 >= r):
            find_count(n-1, l-rN, r-rN, count_dict)
        
    return
    
    
    

def solution(n, l, r):
    answer = 0
    
    # divide and conquer
    one_dict = {i:4**i for i in range(n+1)}
    count_dict = {i:0 for i in range(n+1)}
    
    find_count(n, l, r, count_dict)
    for key, value in count_dict.items():
        answer += value * one_dict[key]
        
    print(count_dict)
    
    return answer



# 1. time out. 직접 배열을 구하는 건 아님.
# number = array([1, 2, 2, 3, 4])
# n = ceil(log(r, 5))
# coeff = 4
# temp = [0, 0, 0, 0, 0]
# for i in range(1, n):
#     number = concatenate([number, (number+coeff), array(temp), \
#              (number+(2*coeff)), (number+(3*coeff))])
#     coeff *= 4
#     temp = temp*5
# number = concatenate([[0], number]) 
# answer = number[r] - number[l-1]