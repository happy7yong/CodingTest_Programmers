function solution(arr) {
    //1. 먼저 현재 배열의 길이 조회
    //2. 다음 배열의 2의 거듭제곱만큼 0추가 
    //2의 0승은 1임!! < 22번 테케 
    let abs = 0;
    
    for(let i=1;true;i*=2){
        if(i >= arr.length){
            //길이보다 큰 첫번째 2의 거듭제곱 
            abs = Math.abs((i) - arr.length)//절대값
            break;
        }
    }
    
    for(let i=0;i<abs;i++){
        arr.push(0)
    }
    return arr;
}