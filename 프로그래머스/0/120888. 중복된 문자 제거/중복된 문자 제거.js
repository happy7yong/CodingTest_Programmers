function solution(my_string) {
    var string = [...my_string]
    var set_char = [...new Set(string)]
    return set_char.join("");
}