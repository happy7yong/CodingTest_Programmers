class priorityQueue{
    //큐 생성자
    constructor(){
        this.queue = [];
    }
    
    //큐 노드 삽입
    enqueue(node, dist){
        this.queue.push({node, dist})
        this.queue.sort((a,b)=>a.dist-b.dist)
        
    }
    
    
    //큐 노드 삭제
    dequeue(){
        if(this.isEmpty()) return null;
        return this.queue.shift();
        
        
    }
    
    //큐가 비었는지 확인
    isEmpty(){
        if (this.queue.length == 0)
            return true;
        return false;
    }
    
}



function solution(n, s, a, b, fares) {
    
    let graph = {}; //인접 그래프 
    

    //입력받은 매개변수를 그래프로 표현
    for(const node of fares){
        if(graph[node[0]]==undefined)
            graph[node[0]] = {};
        if(graph[node[1]]==undefined)
            graph[node[1]] = {};
        
        graph[node[0]][node[1]]=node[2]
        graph[node[1]][node[0]]=node[2]
    }
    
    
    function dijkstra(startnode){
        let distance ={}; //거리의 값 
        let dq = new priorityQueue(); //우선순위 큐는 현재까지의 노드의 최단거리를 갱신함.
    
                                 
                                 
        //모든 값을 무한으로 초기화
        for(let num in graph){ 
            distance[num] = Infinity; //초기엔 모든 거리값이 무한
        }



            distance[startnode] = 0;
            dq.enqueue(startnode,0)


            while(!dq.isEmpty()){        

                let {node, dist} = dq.dequeue(); //현재 위치한 노드
                
                if(dist > distance[node]) continue;

                for(let neighhood in graph[node]){
                    let newDist = distance[node] + graph[node][neighhood]
                    if(newDist < distance[neighhood]){
                        distance[neighhood] = newDist;
                        dq.enqueue(neighhood,newDist)
                    }
                }
            }
        
        return distance
    }

    let startNode = dijkstra(s)
    let destiANode = dijkstra(a) //a에서 공유지점으로
    let destiBNode = dijkstra(b) //b에서 공유지점으로 
    
    let minCost = Infinity;
    
    for(let node =1; node <= n;node++){
        let share = startNode[node];
        let distA = destiANode[node];
        let distB = destiBNode[node];
        if(!share && !distA && !distB ) continue; 
        if(share !== Infinity && distA !== Infinity && distB !== Infinity){
            minCost = Math.min(minCost, share + distA + distB);   
        }
    }

    
    return minCost;
}