# 알고리즘 tree 혹은 binary search
# 자료구조 tree 혹은 list
# 주의: curr과 child 노드의 업데이트 주의. curr을 업데이트, child 만들어서 다음 순번으로 넘기기.
#       class의 메소드의 매개변수의 default value는 전체 class 가 공유. 즉 [] 처럼 객체를 선언하면 그거 하나 공유하는것임..

class tree:
    def __init__(self):
        self.root = node('root')
        self.rootreverse = node('root')
        
    def putString(self, string):
        self.putStringForward(string, self.root)
        self.putStringForward(string[::-1], self.rootreverse)
        
    
    def putStringForward(self, string, root):
        curr = root
        str_len = len(string)

        for index, s in enumerate(string):
            flag = True
            c = curr.getchild(s)
            if c is not None:
                curr.word_dict[str_len-index] = curr.word_dict.setdefault(str_len-index, 0) + 1
                curr = c
            else:
                newNode = node(s, parent=curr)
                curr.child.append(newNode)
                curr.word_dict[str_len-index] = curr.word_dict.setdefault(str_len-index, 0) + 1
                curr = newNode
                
                
    def search(self, query):
        length = len(query)
        curr = self.root
        
        if query == "?"*length:
            return curr.word_dict[length] if length in curr.word_dict else 0
        
        query = list(query)
        if query[0] == "?":
            curr = self.rootreverse
            query = query[::-1]
            
        wild = query.count("?")
        for s in query:
            if s != "?":
                curr = curr.getchild(s)
                if curr is None:
                    return 0
            else:
                return curr.word_dict[wild] if wild in curr.word_dict else 0
                    

class node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.child = list()
        self.word_dict = dict()
        
    def get(self, length):
        if length in self.word_dict:
            return word_dict[length]
        else:
            return 0
        
    def getchild(self, value):
        for c in self.child:
            if c.value == value:
                return c
        return None
        

def solution(words, queries):
    answer = []
    words_tree = tree()
    for word in words:
        words_tree.putString(word)
    
    for query in queries:
        answer.append(words_tree.search(query))
    
    return answer