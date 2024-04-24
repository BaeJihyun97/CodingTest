# union & find 알고리즘

def find(v, union):
    if union[v] != v:
        union[v] = find(union[v], union)
    return union[v]
    

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    union = [i for i in range(n)]
    count = 0
    
    while count < n-1 and len(costs) > 0:
        [n1, n2, cost] = costs.pop(0)
        f1, f2 = find(n1, union), find(n2, union)
        if f1 != f2:
            
            count += 1
            answer += cost
            
            # 주의! 최종 parent의 값을 바꿔야함. n1, n2가 아님!!!!
            value = min(f1, f2)
            union[f1] = value
            union[f2] = value
            
            # print(union)
            
    return answer