function solution(cipher, code) {
    var answer = [];
    var code_c = 0;
    var cipher_str = [...cipher];
    for(let i=1;code_c<cipher_str.length;i++){
        code_c=code*i
        answer.push(cipher_str[code_c-1])
    }
    return answer.join("");
}