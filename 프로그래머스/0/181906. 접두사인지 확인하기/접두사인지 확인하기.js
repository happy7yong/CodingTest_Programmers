function solution(my_string, is_prefix) {
    var answer = 0;
    return my_string.indexOf(is_prefix) == 0 ? 1 : 0;
}