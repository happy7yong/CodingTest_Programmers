function solution(prices) {
    //기준 : 하나의 주식을 기준
    //초단위로 기록된 주식가격이 담김.
    //가격이 떨어지지 않은 기간은 몇초인가?
    
    //prices의 각 요소보다 떨어진 순간 찾기
    //
    
    //i보다 뒤에 있는 요소들이 i값보다 클때동안 count++증가하다가 i>n 일경우 멈춤
    //O(n^2)?
    let count = 0;
    let answer = [];
    
    
    for(let i=0;i<prices.length;i++){
        for(let idx=i;idx<prices.length;idx++){
            if(idx==i) continue;
            count++;
            
            if(prices[i]>prices[idx]){
                break;
            }
            
        }
        answer.push(count);
        count=0;
        
    }

    
    
    return answer;
}