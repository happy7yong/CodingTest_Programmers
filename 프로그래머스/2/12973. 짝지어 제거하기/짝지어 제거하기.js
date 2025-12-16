function solution(s)
{
    var answer = -1;
    //스택
    const string = [...s];
    let stack = [];
    
    //먼저 넣기 아무것도 없을 경우 넣기 
    for(const ch of string){
        if(stack.length && stack[stack.length-1] ===  ch){
           stack.pop();
        }else{
            stack.push(ch);
        }
    }
    



    
    return stack.length ? 0:1;
}