function solution(arr, flag) {
    var answer = [];
    flag.forEach((num,index)=>{
        if(num){
            for(let i=0;i<arr[index]*2;i++){
                answer.push(arr[index])   
            }
        }else{
            for(let i=0;i<arr[index];i++){
                answer.pop()
            }
        }
    })
    return answer;
}