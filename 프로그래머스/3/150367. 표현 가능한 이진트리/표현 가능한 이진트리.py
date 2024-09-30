# Divide & Conquer

def make_binary(number):
    number_ = ""
    while number > 0:
        number_ = str(number % 2) + number_
        number //= 2
    
    i = 1
    while 2**i - 1 < len(number_): i += 1
    
    number_ = "0"* (2**i - 1 - len(number_)) + number_
    
    return number_

def check(num_string, zero=False):
    if len(num_string) <= 1:
        if zero and num_string == "1":
            return False
        return True
    
    mid = len(num_string) // 2
    left_string = num_string[:mid]
    right_string = num_string[mid+1:]
    
    if num_string[mid] == "0":
        return not ("1" in num_string)
    else:
        return check(left_string, zero=False) and check(right_string, zero=False)

def solution(numbers):
    answer = []
    answer = [1 if check(make_binary(n)) else 0 for n in numbers]
    return answer