function solution(arr, k) {
    var answer = [];
    //배열안에 서로다른 k개의 수를 저장함
    //1. set으로 중복 제거 
    //k는 배열의 크기 
    let set = new Set(arr)
    let arrSet = [...set]
    let mp = arrSet.length
    
    if(arrSet.length > k){
        return arrSet.slice(0,k)
    }else if(arrSet.length < k){
        for(let i=0;i<k-mp;i++){
            arrSet.push(-1)
        }
    }
    
    
    return arrSet;
}