function solution(code) {
    var answer = '';
    var codeArr = [...code];
    var mode = 0;
    codeArr.forEach((value, idx)=>{
        if(value==1 && mode==1){
            mode = 0
        }else if(value==1 && mode==0){
            mode = 1
        }
        
        if(value != 1){
            if(mode==0){//0일때
                if(idx%2==0){//짝수
                   answer+=value
                }   
            }else if(mode==1){
                if(idx%2!=0){//홀수
                    answer+=value
                }
            }

        }
    })
    return answer.length==0?"EMPTY":answer;
}