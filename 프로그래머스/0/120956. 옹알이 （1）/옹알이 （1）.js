function solution(babbling) {
    var pron = ["aya","ye","woo","ma"];//조합이 가능해야됨
    var answer = [];
    for(let i=0;i<pron.length;i++){
        for(let j=0;j<babbling.length;j++){
            babbling[j] = babbling[j].split(pron[i]).filter(num=>num.length!=0).join(" ")
        }
        console.log(babbling)
    }
    
    return babbling.filter(num=>num.length==0 || num==" ").length;
}