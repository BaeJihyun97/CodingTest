def solution(sequence, k):
    # 포인터 두개 쓰는 전형적인 문제
    # start, end 두기
    
    # STEP1: end값 찾기
    # senquence[end] 값이 k 보다 큰 것은 볼 필요 없음 
    end = len(sequence)-1
    while sequence[end] > k:
        end -= 1
    
    # STEP2: start, sumv 값 초기화
    # end == start 로 두고, start를 한칸씩 빼기
    # 왜냐 가장 짧은 수열을 찾는 것이니 큰 수를 먼저 넣어야함(그리디)
    start = end
    sumv = sequence[end]
    
    # STEP3: start, end 움직이며 k 값 찾기
    # True로 둬도 상관 없음. 
    # boundary 값은 문제에서 항상 답이 존재한다고 했으니 확인할 필요 없음. 
    while start <= end: 
        if sumv == k: # 같을 때는 멈추기
            break
        elif sumv < k: # sumv 가 더 작다면 start 왼쪽으로해서 더하기
            start -= 1
            sumv += sequence[start]
        else: # sumv > k, sumv가 더 크다면, sequence[end]를 포함하는 답이 없으니 end 값 왼쪽으로 옮기기
            # 이 코드는 항상 start < end 인 상황일 때.
            sumv -= sequence[end]
            end -= 1
            # 만일 STEP1을 하지 않으면 start == end 일때 end -= 1이 됨으로 예상치 않은 동작을 함
            # start == end 인 경우를 확인하고 따로 해줘야함.

    # STEP4: 길이가 짧은 수열이 여러 개인 경우 가장 작은 인덱스 찾기
    # 이 경우는 모든 배열이 같은 수일 때. 
    while start > 0 and sequence[start-1] == sequence[end]:
        start -= 1
        end -= 1
    
    answer = [start, end]
    return answer