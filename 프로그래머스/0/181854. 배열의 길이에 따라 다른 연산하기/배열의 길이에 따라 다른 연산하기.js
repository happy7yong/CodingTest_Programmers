function solution(arr, n) {
    var answer = [];
    let start = 0;
    
    if(arr.length%2!=0){
        start = 0;
    }else if(arr.length%2==0){
        start = 1;
    }
    
    for(let i=start;i<arr.length;i+=2){
            arr[i]=arr[i]+n
        }
    return arr;
}