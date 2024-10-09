import sys
sys.setrecursionlimit(300000)

MAXSALE = 2**31-1

def dfs(curr, tree, dp, sales):
    if curr not in tree.keys():
        dp[curr][0] = 0
        dp[curr][1] = sales[curr]
        return
    
    minimum1, diff, count = 0, [], 0
    for p in tree[curr]:
        dfs(p, tree, dp, sales)
        if dp[p][1] <= dp[p][0]:
            count += 1
            minimum1 += dp[p][1]
        else:
            minimum1 += dp[p][0]
        diff.append(dp[p][1]-dp[p][0])
    
    dp[curr][1] = minimum1 + sales[curr]
    if count > 0:
        dp[curr][0] = minimum1
    else:
        dp[curr][0] = minimum1 + min(diff)

    return         

def solution(sales, links):
    sales = [0] + sales
    selected = [False for _ in range(len(sales))]
    dp = [[MAXSALE, MAXSALE] for _ in range(len(sales))]
    # tree 만들기
    tree = dict()
    for p, c in links:
        if p in tree:
            tree[p].append(c)
        else:
            tree[p] = [c]
            
    leaders = list(tree.keys())
    
    dfs(1, tree, dp, sales)
    
    
    return min(dp[1][0], dp[1][1])