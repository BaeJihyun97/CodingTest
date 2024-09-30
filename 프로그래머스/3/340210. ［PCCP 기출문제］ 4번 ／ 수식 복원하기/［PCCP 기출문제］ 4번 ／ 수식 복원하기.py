from copy import deepcopy

def make_decimal_system(number, n_system):
    number_, r = 0, 1
    while number > 0:
        number_ += (number % 10) * r
        number //= 10
        r *= n_system
    return number_

def make_n_system(number, n_system):
    if number == 0:
        return "0"
    
    number_ = ""
    while number > 0:
        number_ = str(number % n_system) + number_
        number //= n_system
    return number_

def calculate(a, b, op, n_system):
    a, b = make_decimal_system(a, n_system), make_decimal_system(b, n_system)
    c = a + b if op =="+" else a - b
    return make_n_system(c, n_system)
    
def check(a, b, op, n_systems):
    number = calculate(a, b, op, n_systems[0])
    for n_system in n_systems[1:]:
        if number != calculate(a, b, op, n_system):
            return "?"
        
    return number
            

def solution(expressions):
    answer = []
    # 리스트로 정리
    expressions_ = []
    expressions_X = []
    numbers = set()
    for expression in expressions:
        a, op, b, _, c = expression.split(" ")
        numbers.update(expression)
        a, b = int(a), int(b)
        if c != 'X':
            c = int(c)
            expressions_.append([a, b, c, op])
        else:
            expressions_X.append([a, b, c, op])
        
    
    # 가능한 진법은 maxN+1 ~ 9 사이
    for c in ['=', '-', '+', ' ', 'X']: numbers.discard(c)
    maxN = max([int(n) for n in numbers])
    
    # 진법 찾기
    n_systems = [i for i in range(maxN+1, 10)]
    if len(n_systems) > 1:
        for a, b, c, op in expressions_:
            c_10 = a + b if op == "+" else a - b
            if c_10 != c:
                n_systems_ = deepcopy(n_systems)
                for i_system in n_systems_:
                    a_10, b_10 = make_decimal_system(a, i_system), make_decimal_system(b, i_system)
                    c_10 = a_10 + b_10 if op =="+" else a_10 - b_10
                    print(i_system, a_10, b_10, c_10, a, b, c)
                    if c_10 != make_decimal_system(c, i_system):
                        n_systems.remove(i_system)
            if len(n_systems) <= 1: break
    

    # 가능한 진법으로 계산하기
    for a, b, c, op in expressions_X:
        c = check(a, b, op, n_systems)
        answer.append(f"{a} {op} {b} = {c}")
            
                

    return answer