function solution(my_string) {
    var answer = '';
    var Str = [];
    var answer_Str = [];
    Str=my_string.split("")
    for(let i=0;i<Str.length;i++){
        if((Str[i]!="u") && (Str[i]!="a") && (Str[i]!="i") && (Str[i]!="e") && (Str[i]!="o")){
            answer_Str.push(Str[i])
        }
    }
    answer=answer_Str.join("");
    return answer;
}