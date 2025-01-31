function solution(my_string, n) {
    var answer = '';
    var str_arr=my_string.split('');
    var answer_arr = [];
    for(let i=0;i<str_arr.length;i++){
        for(let j=0;j<n;j++){
            answer_arr.push(str_arr[i])
        }
    }
    answer=answer_arr.join('')
    return answer;
}