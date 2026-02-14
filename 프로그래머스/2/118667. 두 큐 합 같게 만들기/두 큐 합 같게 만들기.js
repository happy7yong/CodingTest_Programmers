function solution(queue1, queue2) {
    var answer = -2;
    //길이가 같은 두개의 큐 queue1.length === queue2.length
    //하나의 큐를 골라 원소 추출
    //추출된 원소를 다른 큐에 넣어서 각 큐의 원소 합이 같도록한다.
    
    //이때 작업 최소 횟수 
    
    //한번의 팝 인서트는 짝ㄱ꿍 : 1회로 침
    //큐는 먼저 집어넣은 원소가 먼저 나오는 구조가 아님
    
    //두큐에 담긴 모든 원소의 합이 30이다.
    //각 큐의 합을 15로 만들어야한다.
    
    //전체 합이 홀수면 절대 두 큐가 같아 질수없다 -> -1
    //1. queue1의 모든 합과 queue2의 모든 합 %2 가 각 큐에 있어야할 합
    
    const queue = [...queue1,...queue2];
    let sum1 = queue1.reduce((a,b)=>a+b);
    
    
    let total = queue.reduce((a,b)=>a+b);

    let target = Math.ceil(total/2);
    
    //한큐만 target에 동일하면된다.
    //투포인터 문제
    //1 2 1 2 | 1 10 1 2
    let startIdx = 0;
    let start = queue[startIdx];
    //이때 start의 로직은 queue1의 길이가 넘어가면 
    //queue1[queue1.length] == queue2[0]
    //queue1[queue1.length+1]==queue2[1]
    let endIdx = queue1.length-1;
    let end = queue[endIdx];
    
    let count = 0;
    let currentSum = sum1;
    
    while(endIdx!=startIdx){
        start = queue[startIdx]
        end = queue[endIdx]
        
        
        if(currentSum < target) {
            endIdx++;
            currentSum += queue[endIdx];
        }else if(currentSum == target){
            return count;
        }else{
            currentSum -= queue[startIdx];
            startIdx++;
        }
        
        count++;
    
        if(endIdx===startIdx && currentSum != target) return -1//닿았는데 currentSum != target인 경우
    
    }
    

    
    //이거 BFS로 풀어야되나? 최선의 방법 찾기는 BFS DFS로 풀지 않나?

    

    
    
    
    return count;
}