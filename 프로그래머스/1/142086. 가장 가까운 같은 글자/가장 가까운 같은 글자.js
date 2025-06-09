function solution(s) {
    var answer = [];
    let lastIndex = 0;
    
    answer = [...s].map((_,idx)=>{
        lastIndex = s.slice(0,idx).lastIndexOf(_);
        if(lastIndex === -1){
            return -1;
        }else{//있을경우
            return idx-lastIndex;
        }
    })
    
     return  answer;
    
}