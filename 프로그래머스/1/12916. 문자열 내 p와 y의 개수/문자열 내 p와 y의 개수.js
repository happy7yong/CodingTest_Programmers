function solution(s){
    
    var stack1 = 0;
    var stack2 = 0;
    var answer = [...s.toLowerCase()]
    for(let i=0;i<answer.length;i++){
       answer[i] == "p" ? stack1 += 1 : 0
       answer[i] == "y" ? stack2 += 1 : 0
    }
    return  stack1==stack2
}