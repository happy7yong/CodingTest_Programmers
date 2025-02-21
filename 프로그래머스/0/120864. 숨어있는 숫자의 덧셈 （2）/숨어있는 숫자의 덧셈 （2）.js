function solution(my_string) {
    var str = [...my_string]
    var stack = [];
    for(let i=0;i<my_string.length;i++){
        if(!isNaN(str[i])){
            if(!isNaN(str[i+1])){
                if(!isNaN(str[i+2])){
                    stack.push(str[i]+str[i+1]+str[i+2])
                    str[i+1]=0
                    str[i+2]=0
                }else{
                    stack.push(str[i]+str[i+1])
                    str[i+1]=0
                }
            }else{
                stack.push(str[i])  
            }
        }
    }
    return stack.length==0?0:stack.map(Number).reduce((acc,cur)=>acc+cur);
}