function solution(num_list) {
    var answer = 0;
    let num_sum = num_list.reduce((acc,rec)=>acc+rec)
    let num_multiply = num_list.reduce((acc,rec)=>acc*rec)
    
    return (num_sum*num_sum > num_multiply) ? 1 : 0;
}