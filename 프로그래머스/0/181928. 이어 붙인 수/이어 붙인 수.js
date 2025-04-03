function solution(num_list) {
    var answer = 0;
    return parseInt(num_list.filter(num=>num%2==0).join("")) + parseInt(num_list.filter(num=>num%2!=0).join(""));
}