function solution(arr) {
    //정사각형으로 만들기
    //arr의 col와 arr의 row값이 같아야됨.
    //row가 더 큰지, col이 더 큰지에 따라 다를 듯 
    
    
    let maxLen = Math.max(arr.length,arr[0].length)
    
    for(let row=0;row<maxLen;row++){ 
        if(!arr[row]){
            arr[row] = []
        }
        
        for(let col=arr[row].length;col<maxLen;col++){
            arr[row].push(0)
        }
        console.log(arr[row])
        
    
    }
    return arr;
}