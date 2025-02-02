function solution(emergency) {
    var answer = [];
    var max = 0;
    var emergency_clone = [...emergency];
    emergency_clone.sort((a,b)=>b-a)
    var k =1;
    for(let i=0;i<emergency_clone.length;i++){
        for(let j=0;j<emergency_clone.length;j++){
            if(emergency[j]==emergency_clone[i]){
                answer[j]=k;
                k++ 
            }   
        }
    }
    
    return answer;
}