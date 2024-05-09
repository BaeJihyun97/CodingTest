from collections import deque

def drop(graph):
    curr = 1
    
    while len(graph[curr]) > 0:
        n_next = len(graph[curr])
        for i in range(n_next):
            if graph[curr][i][1]:
                curr = graph[curr][i][0]
                break

    return curr

def changeGraph(graph):
    curr = 1
    while len(graph[curr]) > 0:
        n_next = len(graph[curr])
        for i in range(n_next):
            if graph[curr][i][1]:
                edge_change = (i+1) % n_next
                graph[curr][i][1] = False
                graph[curr][edge_change][1] =True
                curr = graph[curr][i][0]
                break

    return 

# -1: 불가, 0: 탐색 필요, 1: 가능
def check(count, target):
    flag = 1
    for c, t in zip(count, target):
        if c > t: 
            return -1
        elif c * 3 < t:
            flag = 0    
    return flag

def search(graph, target, n_node):
    answer = []
    count = [0 for _ in range(n_node+1)]
    leaf_nodes = []
    
    while check(count, target) == 0:
        leaf = drop(graph)
        leaf_nodes.append(leaf)
        count[leaf] += 1
        changeGraph(graph)
    
    number_dict = dict()
    if check(count, target) > 0:
        for i, (c, t) in enumerate(zip(count, target)):
            temp = []
            n1 = max((3 * c -t)//2, 0) # 1의 개수
            c_, t_ = c - n1, t - n1
            n2 = 3 * c_ - t_
            n3 = t_ - 2 * c_
            temp += [1 for _ in range(n1)]
            temp += [2 for _ in range(n2)]
            temp += [3 for _ in range(n3)]
            number_dict[i] = temp
            
        for node in leaf_nodes:
            answer.append(number_dict[node].pop(0))
        return answer
            
    else:
        return [-1]


        

    

def solution(edges, target):
    answer = []
    target.insert(0, 0)
    
    # make graph 
    n_node = max(map(max, edges))
    graph = [[] for _ in range(n_node+1)]
    count = [0 for _ in range(n_node+1)]
    for [p, c] in edges:
        graph[p].append([c, False])
        
    for node in graph:
        node.sort()
        if len(node) != 0:
            node[0][1] = True
            
    # Greedy?
    return search(graph, target, n_node)