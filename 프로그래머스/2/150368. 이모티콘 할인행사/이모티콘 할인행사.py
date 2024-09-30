def calculate(discounts, users, emoticons):
    plus_n, sales = 0, 0
    emoticons_ = list(zip(discounts, emoticons))
    for user in users:
        percent, thr_price = user
        tot_price = sum([p * (100-d) // 100 for d, p in emoticons_ if d >= percent ])
        if tot_price >= thr_price:
            plus_n += 1
        else:
            sales += tot_price  
    return plus_n, sales


def dfs(discounts, depth, max_depth, users, emoticons):
    if depth == max_depth:
        return calculate(discounts, users, emoticons)
    
    plus_n, sales = 0, 0
    for disc in [10, 20, 30, 40]:
        plus_n_, sales_ = dfs(discounts+[disc], depth+1, max_depth, users, emoticons)
        if plus_n < plus_n_:
            plus_n, sales = plus_n_, sales_
        elif plus_n == plus_n_ and sales < sales_:
            plus_n, sales = plus_n_, sales_
            
    return plus_n, sales


def solution(users, emoticons):
    return dfs([], 0, len(emoticons), users, emoticons)