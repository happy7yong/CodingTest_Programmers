function solution(my_string) {
    let str = [...my_string];
    //기존 문자열은 알파벳수만큼 있어야됨.
    let apb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    let answer = Array(apb.length).fill(0);
    str.forEach(_=>{
        if(apb.indexOf(_)!==-1) {
            answer[apb.indexOf(_)]++
        }
    })
    
    
    
    return answer;
}