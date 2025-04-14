function solution(binomial) {
    var answer = binomial.split(" ")
    var num = [...answer].map(Number)
    console.log(num, binomial)
    
    if(answer[1]=="+"){
        return num[0]+num[2]      
    }else if(answer[1]=="-"){
        return num[0]-num[2]
    }else{
        return num[0]*num[2]
    }
}