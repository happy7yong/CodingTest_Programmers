function solution(my_string, is_suffix) {
    var answer = 0;
    let my_reverse = [...my_string].reverse().join();
    let index_reverse = [...is_suffix].reverse().join();

    return my_reverse.indexOf(index_reverse)==0 ? 1 : 0;
}