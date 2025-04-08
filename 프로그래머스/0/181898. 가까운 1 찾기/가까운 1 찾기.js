function solution(arr, idx) {
    let answer = -1;
    for(let i=1;i<=arr.length;i++){
        if(i>idx && arr[i-1]==1){
            answer = i-1;
            break;
        }
    }
    return answer;
}