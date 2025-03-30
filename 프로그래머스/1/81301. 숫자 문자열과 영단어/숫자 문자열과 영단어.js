function solution(s) {
    let num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    let i = 0;

    while(isNaN(s)){
        s=s.replaceAll(num[i], i)
        i++
    }
    
    return parseInt(s);
}