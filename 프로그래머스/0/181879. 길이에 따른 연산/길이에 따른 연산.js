function solution(num_list) {
    var answer = 0;
    if(num_list.length >= 11) {
        answer = num_list.reduce((acc,rec)=>acc+rec)
    }else{
        answer = num_list.reduce((acc,rec)=>acc*rec)
    }
    
    return answer;
}