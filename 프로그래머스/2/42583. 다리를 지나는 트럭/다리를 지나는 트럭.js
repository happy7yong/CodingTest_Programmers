function solution(bridge_length, weight, truck_weights) {
    
    //트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순서대로 건넘.
    //모든 트럭이 다리를 건너려면 최소 몇초가 걸릴까요?
    //다리에는 트럭 <= bridge_length 
    // trunck[current]+trunck[current+1] > 0 ? +시간 : 다리로 옮겨 
    //다리 <= weight
    //다리에 완전히 오르지 않을경우 무시
    //큐, 스택
    //무게가 10kg(weight)
    
    let truck_success = []; //다리를 지난 트럭
    
    let len = truck_weights.length; //건너야할 트럭 갯수
    let time = 0;//총 경과시간
    
    let bridge = [];//다리를 건너는 트럭
    let current_truck = 0;
    
    //다리를 건너는 트럭은 각 count를 가지고 있다. 
    //다리에 오른 트럭들의 time을 보관하는 모음집
    let current_time = [];
    //트럭들은 기존에 본인이 몇번인지 알고있어야한다.
    //7->0번, 4->1번, 5->2번
    let truck_order = [...truck_weights];
    
    let head_time = 0;
    
    let bridge_first = 0;

     while(truck_success.length != len){
         time++;//시간이 지남
        
         //헤드에서 트럭을 뺐음 
         current_truck = truck_weights.shift();
         
         //다리에 있는 트럭 모두 +1
         current_time = current_time.map(i=>i+1);
         
                            //현재 다리를 건너는 트럭의 헤드
         head_time = current_time[0];
                  //가장 앞에 다리를 건너는 트럭의 수가 length보다 증가할경우 
         if(head_time > bridge_length){
             truck_success.push(bridge.shift());
             current_time.shift();
             
         }
         
         if((bridge.length == 0) || (bridge.reduce((a,b)=>a+b) + current_truck <= weight)){
            bridge.push(current_truck);
            current_time.push(1);
         }else{
             //다시 대기 앞에 넣음 - 원래 있던 곳으로
             truck_weights.unshift(current_truck );
         }
         
         
     }
    
    
    return time;
}