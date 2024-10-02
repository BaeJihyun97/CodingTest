import sys
sys.setrecursionlimit(300000000)

def dfs(n, m, x, y, r, c, k, depth, path):
    # print(path)
    if depth == k:
        if x == r and y == c:
            return path
        else:
            return 'impossible'
        
    dist = abs(x - r) + abs(y - c)
    if dist > k - depth:
        return 'impossible'
    
    ans = 'impossible'    
    for d, dr, dc in [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]:
        new_x, new_y = x + dr, y+dc
        if new_x >= 0 and new_x < n and  new_y >= 0 and new_y < m:
            ans = dfs(n, m, new_x, new_y, r, c, k, depth+1, path+d)
            if ans != 'impossible':
                break
    return ans

def solution(n, m, x, y, r, c, k):
    answer = ''
    diff = k - (abs(x-r) + abs(y-c))
    if diff < 0 or diff % 2 != 0:
        return 'impossible'
    return dfs(n, m, x-1, y-1, r-1, c-1, k, 0, "")