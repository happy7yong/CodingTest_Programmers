function solution(my_string, index_list) {
    var answer = '';
    let index = index_list.map(num=>my_string[num])
    return index.join("");
}