function solution(arr, queries) {
    //queries에 있는 값을 하나씩 더함.
    queries.forEach((it)=>{
        let [start, end] = it
        for(let i = start;i<=end;i++){
            arr[i]++
        }
    })
    
    return arr;
}