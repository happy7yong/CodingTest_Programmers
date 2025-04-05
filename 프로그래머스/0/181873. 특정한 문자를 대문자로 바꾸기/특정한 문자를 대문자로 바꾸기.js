function solution(my_string, alp) {
    var answer = '';
    //alp를 찾아서 해당 문자를 대문자로
    let str = [...my_string]
    let index = str.indexOf(alp)
    
    if(index > -1){
        return my_string.replaceAll(alp, alp.toUpperCase())
    }else{
        return my_string
    };
}