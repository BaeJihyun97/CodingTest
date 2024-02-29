# 부분합!
# 부분 수열의 합은 구간합 생각하기
# S(i~j) = S(j) - S(i)

def solution(sequence):
    
    length = len(sequence)
    ls = [0] * (length+1)
    for index in range(length):
        ls[index+1] = ls[index] + sequence[index]*(-1)**index
    # print(ls)
    answer = max(ls) - min(ls)
    return answer