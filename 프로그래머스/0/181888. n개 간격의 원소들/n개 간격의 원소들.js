function solution(num_list, n) {
    var answer = [];
    answer = num_list.filter((_,i)=>i%n==0)
    return answer;
}