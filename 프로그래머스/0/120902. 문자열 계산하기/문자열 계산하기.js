function solution(my_string) {
    var str = my_string.split(" ")
    var num = str.map(Number)
    for(let i=0;i<str.length;i++){
        if(str[i]=="+"){
            num[i+1] = num[i-1]+num[i+1]
        }else if(str[i]=="-"){
            num[i+1] = num[i-1]-num[i+1]
        
        }   
    }
    return num[str.length-1]

}