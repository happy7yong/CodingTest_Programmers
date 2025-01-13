function solution(s) {
    var answer = '';
    var answer_str=s.split(" ");
    
    for(let i=0;i<answer_str.length;i++){
        answer_str[i]=parseInt(answer_str[i]);
    }
    
    var max = answer_str[0];
    var min = answer_str[0];
   
    
    for(let i=0;i<answer_str.length;i++){
        if(min>answer_str[i]){
            min=answer_str[i];
        }
        
        if(max<answer_str[i]){
            max=answer_str[i];
        }
    }
    
    
    var sum_maxmin=[min,max];
    sum_maxmin=sum_maxmin.join(' ');
    
    return sum_maxmin;
}