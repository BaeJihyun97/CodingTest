import re

def solution(word, pages):
    url_content = re.compile('<meta property="og:url" content=\"https://(\S+)\"')
    url_external = re.compile('<a href=\"https://[^\s]+\">')
    word = re.compile(' '+word+' ', re.I)
    
    score = [0 for _ in range(len(pages))]
    link_count = [0 for _ in range(len(pages))]
    link_dict = dict()
    link_index = dict()
    
    
    for index, page in enumerate(pages):
        url = url_content.search(page).group().split('\"')[3]
        url_ex = [u.split('\"')[1] for u in url_external.findall(page)]
        # print(url)
        
        link_dict[url] = url_ex
        link_index[url] = index
        
        body = re.sub('[^a-zA-Z]', ' ', page)
        body = re.sub('[\s]+', '  ', body)
        
        score[index] += len(word.findall(body)) # 기본 점수
        link_count[index] = score[index] / len(url_ex) if len(url_ex) > 0 else 0
    
    link_list = [key for key in link_index.keys()]
    for url, links in link_dict.items():
        for l in links:
            if l in link_list and url in link_list: 
                score[link_index[l]] += link_count[link_index[url]]

    return score.index(max(score))