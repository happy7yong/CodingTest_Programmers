function solution(s){
    var answer = true;
    var str = [];
    var stack = [];
    var basket_str = "";
    var basket_stack="";
    
    str=s.split("");
    
    for(let num of str){
        basket_str=num;
        if("("==basket_str){
            stack.push(basket_str);
        }else if(")"==basket_str){
            if(stack.length==0){
                answer=false;
                break;
            }else{
                stack.pop();
            }
        }
    }
    
    if(0 != stack.length){
        answer=false;
    }
    
    
    return answer;
}