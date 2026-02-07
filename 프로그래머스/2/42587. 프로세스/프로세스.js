function solution(priorities, location) {
    var answer = 0;
    let queue = [...priorities];
    
    
    //프로세스 [ABCD] => [2,1,3,2]
    //숫자가 높을수록 우선순위가 높음


    //1. 우선 가장 앞에있는 프로세스 꺼냄
        //2. 큐에 더 높은 우선순위있는지 조회
            //2-1. 있음 -> 맨뒤에 넣음
            //2-2. 없음 -> 제거
    //3. 반복

    priorities[location] //이 자식이 location 그 인스턴스인지 어떻게 알아?
    
    let currentLocation = location;
    let len = priorities.length;

    let Qprev = 0;
    let count = 0;
    
    let prevQueue = 0;
    let currentQueue = 0;
    
    while(queue.length!=0){
        prevQueue = queue.length;
        Qprev = queue.shift();
        if(queue.some(i => Qprev < i)){

            if(currentLocation==0){
                queue.push(Qprev)
                currentLocation=queue.length-1;
            }else{
                queue.push(Qprev)
                currentLocation--;
            }
        }else{

            
            currentQueue = queue.length;
            if(currentQueue!=prevQueue){
                count++;
            }
            if(currentLocation==0){
                return count;
            }
            currentLocation--;
        }

    }
    

}