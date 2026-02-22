function solution(n, times) {
    //입력값이 너무 크다.
    //모든 사람이 심사를 받는게 최솟값을 구하고 싶다. -> 이분 탐색인가 의심
    
    let left = 1;
    let right = Math.max(...times)*n;
    let answer = 0;
    
    
    while(left <= right){
        let mid = Math.floor((left+right)/2);
        
        let total = 0;
        //심사량 20초동안 몇명했는지 
        for(let time of times){
            total += Math.floor(mid / time);
        }
        
        if(total >= n){
            answer = mid;
            right = mid -1;
        }else {
            left = mid + 1;
        }
        
    }
    return answer;
}