function solution(arr, queries) {
    var answer = [];
    //i가 k의 배수? 0<i<4 i가 0 1 2 3 4 인데 1의 배수 
    for(let q of queries){
        let [start, end, k] = q
        for(let i=start;i<=end;i++){
            if(i%k==0) arr[i]++
        }
    }
    return arr;
}