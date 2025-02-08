function solution(my_string, num1, num2) {
    var my_str = [...my_string]
    let m = 0;
    
    for(let i=0;i<my_str.length;i++){
        if(num1==i){
            m=my_str[num1]
            my_str[num1]=my_str[num2]
            my_str[num2]=m
        }
    }
    
    return my_str.join("");
}