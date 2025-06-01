function solution(my_string, queries) {
    var answer = '';
    let string_arr = [...my_string]
    for( let [start, end] of queries){
        let slice_arr = string_arr.slice(start, end+1).reverse(); //자르고 돌리기
        string_arr = [
            ...string_arr.slice(0, start),
            ...slice_arr,
            ...string_arr.slice(end + 1)
        ];
        
    }
    return string_arr.join("");
}