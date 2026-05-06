from collections import defaultdict
from collections import deque

def can_diff(word1, word2):
    count = 0;
    
    for i in range(len(word1)):
        if word1[i] != word2[i] :
            count+=1;
        
    return count == 1;
        
def solution(begin, target, words):
    answer = 0
    
    
    graph = defaultdict(set);
    visited = set([begin]);
    words.append(begin)
    
    #노드 연결하기 : 인접 리스트로 만들기
    for word1 in words :
        for word2 in words :
            if can_diff(word1,word2) :
                graph[word1].add(word2)
                graph[word2].add(word1)
    
    
    #방문 노드 만들기
    #인접 행렬에서는 거리 저장하는 방법 : dict 배열만들어서 distance[nextNode] = distance[curNode] + 1
    #이렇게 했었는데 인접 리스트에서는 큐안에 거리를 함께 페어로 묶어서 다닌다고 함.
    #queue.append((node, dist))
    
    
    queue = deque([(begin,0)]);

    while(queue) :
        curNode,dist = queue.popleft()
        
        if curNode == target :
            return dist
        
        for nextNode in graph[curNode] :
            if nextNode not in visited :
                visited.add(nextNode);
                queue.append((nextNode,dist+1))
            
    
    return 0

#dp아님?
#깊이 우선 bfs로 풀어야할것같은데
#bfs가 필요한것 :
#1. 큐안에 탐사 큐 들어가야됨.
#2. 방문확인할 노드
#3. 시작 노드

#어떻게 map을 그릴지가 중요할것같은데
#정렬할까 hit -> cog

#단어 하나를 노드로 보고 
#한글자만 다른 단어끼리 간선으로 연결되어있다고 생각하기.
#hit - hot - dot - dog - log - lot
#                            - cog
#간선으로 연결되어있음. 그럼 연결시켜야되는거아님? 지금은 배열인 상태인거잖음

#노드의 연결 : 간선 연결리스트 말고 
# hot : hit, dot
# dot : dot, hot 이런식으로 배열만들기

