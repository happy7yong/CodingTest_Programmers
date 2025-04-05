function solution(num_list) {
    var answer = [];
    num_list.sort((a,b)=>b-a)
    for(let i=0;i<5;i++){
        num_list.pop()
    }
    return num_list.reverse();
}