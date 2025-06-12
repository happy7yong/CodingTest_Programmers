function solution(numLog) {
    let Str = "";
    let answer = numLog.forEach((Num,i)=>{
        let preNum = numLog[i-1];
        let dif = Num - preNum;
        if(i>0) Str += dif == 1 ? "w" : dif == -1 ? "s" : dif == 10 ? "d" : "a"
    })
    return Str ;
}